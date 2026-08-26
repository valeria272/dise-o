// Estado del portal: vive en un Google Sheet (chunks de 45k por celda, columna A).
// Autenticación: refresh token OAuth compartido del monorepo (solo en memoria, nunca se reescribe).
const CH = 45000;

async function accessToken() {
  const r = await fetch("https://oauth2.googleapis.com/token", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: process.env.G_CLIENT_ID,
      client_secret: process.env.G_CLIENT_SECRET,
      refresh_token: process.env.G_REFRESH_TOKEN,
      grant_type: "refresh_token",
    }),
  });
  if (!r.ok) throw new Error("oauth " + r.status);
  return (await r.json()).access_token;
}

async function readState(at) {
  const r = await fetch(
    `https://sheets.googleapis.com/v4/spreadsheets/${process.env.SHEET_ID}/values/estado!A1:A100`,
    { headers: { Authorization: `Bearer ${at}` } }
  );
  if (!r.ok) throw new Error("sheets read " + r.status);
  const rows = (await r.json()).values || [];
  const js = rows.map((x) => x[0] || "").join("");
  if (!js.trim()) return { entrega: "", cliente: "Hilton", pieces: [], queue: [] };
  return JSON.parse(js);
}

async function writeState(at, state) {
  const js = JSON.stringify(state);
  const chunks = [];
  for (let i = 0; i < js.length; i += CH) chunks.push([js.slice(i, i + CH)]);
  while (chunks.length < 100) chunks.push([""]);
  const r = await fetch(
    `https://sheets.googleapis.com/v4/spreadsheets/${process.env.SHEET_ID}/values/estado!A1:A100?valueInputOption=RAW`,
    {
      method: "PUT",
      headers: { Authorization: `Bearer ${at}`, "Content-Type": "application/json" },
      body: JSON.stringify({ values: chunks }),
    }
  );
  if (!r.ok) throw new Error("sheets write " + r.status);
}

function isPin(pin) {
  return typeof pin === "string" && pin === process.env.PORTAL_PIN;
}

// ---- Trello (cola de solicitudes = tablero HILTON; la KAM lo ordena los viernes) ----
function trelloOn() {
  return !!(process.env.TRELLO_KEY && process.env.TRELLO_TOKEN && process.env.TRELLO_BOARD_HILTON);
}
function trelloAuth() {
  return `key=${process.env.TRELLO_KEY}&token=${process.env.TRELLO_TOKEN}`;
}
async function trelloGet(path, params = "") {
  const r = await fetch(`https://api.trello.com/1/${path}?${trelloAuth()}${params}`);
  if (!r.ok) throw new Error("trello get " + r.status);
  return r.json();
}
async function trelloPost(path, params) {
  const q = new URLSearchParams(params).toString();
  const r = await fetch(`https://api.trello.com/1/${path}?${trelloAuth()}&${q}`, { method: "POST" });
  if (!r.ok) throw new Error("trello post " + r.status);
  return r.json();
}
async function trelloBoard() {
  const b = process.env.TRELLO_BOARD_HILTON;
  const [lists, cards] = await Promise.all([
    trelloGet(`boards/${b}/lists`, "&fields=name,id,pos"),
    trelloGet(`boards/${b}/cards`, "&fields=name,idList,pos,labels,due&limit=200"),
  ]);
  return { lists, cards };
}

// ---- Carpetas de Drive: <raíz>/<Entrega>/<Marca>/<Categoría> ----
const MARCA_NOMBRE = {
  DT: "DoubleTree", QB: "QB Restaurant", BW: "Between", P18: "Piso18",
};
function limpio(s, fallback) {
  const t = String(s == null ? "" : s).replace(/[\/\\:*?"<>|]/g, "-").trim().slice(0, 60);
  return t || fallback;
}

// Busca una subcarpeta por nombre; si no existe, la crea. Devuelve su id.
async function carpetaHija(at, padreId, nombre) {
  const q = encodeURIComponent(
    `name='${nombre.replace(/'/g, "\\'")}' and '${padreId}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false`
  );
  const r = await fetch(`https://www.googleapis.com/drive/v3/files?q=${q}&fields=files(id,name)&pageSize=1`, {
    headers: { Authorization: `Bearer ${at}` },
  });
  if (r.ok) {
    const encontrada = (await r.json()).files || [];
    if (encontrada.length) return encontrada[0].id;
  }
  const c = await fetch("https://www.googleapis.com/drive/v3/files?fields=id", {
    method: "POST",
    headers: { Authorization: `Bearer ${at}`, "Content-Type": "application/json" },
    body: JSON.stringify({
      name: nombre,
      mimeType: "application/vnd.google-apps.folder",
      parents: [padreId],
    }),
  });
  if (!c.ok) throw new Error("drive mkdir " + c.status);
  return (await c.json()).id;
}

// Devuelve la carpeta destino, creando el árbol si hace falta.
// Si algo falla, cae a la raíz para no bloquear la subida.
async function carpetaDestino(at, { entrega, marca, cat }) {
  const raiz = process.env.DRIVE_FOLDER_ID;
  try {
    const nivel1 = await carpetaHija(at, raiz, limpio(entrega, "Sin entrega"));
    const nivel2 = await carpetaHija(at, nivel1, MARCA_NOMBRE[marca] || limpio(marca, "Otras"));
    const nivel3 = await carpetaHija(at, nivel2, limpio(cat, "Otros"));
    return nivel3;
  } catch (e) {
    return raiz;
  }
}

module.exports = { accessToken, readState, writeState, isPin, trelloOn, trelloGet, trelloPost, trelloBoard, carpetaDestino };
