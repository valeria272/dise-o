const { accessToken, readState, writeState, isPin, trelloOn, trelloGet, trelloPost } = require("./_lib");

const ADMIN = new Set([
  "piece_add", "piece_edit", "piece_img", "piece_del", "comment_resolve", "piece_fmt", "archivar",
  "queue_add", "queue_move", "queue_state", "queue_del",
  "entrega", "clear", "ping",
]);

const LISTA_POR_MARCA = { DT: "DOUBLETREE", QB: "QB", BW: "BETWEEN", P18: "PISO18" };

// Crea la tarjeta en el tablero de Trello que la KAM ordena los viernes.
async function trelloQueueAdd(b) {
  const board = process.env.TRELLO_BOARD_HILTON;
  const [lists, labels] = await Promise.all([
    trelloGet(`boards/${board}/lists`, "&fields=name,id"),
    trelloGet(`boards/${board}/labels`, "&fields=name,id&limit=50"),
  ]);
  const quiero = LISTA_POR_MARCA[b.marca] || "DOUBLETREE";
  const list = lists.find((l) => l.name.toUpperCase().includes(quiero)) || lists[0];
  const lbl = labels.find((l) => (l.name || "").toUpperCase() === "POR DESARROLLAR");
  const desc = [
    b.tipo ? "Tipo: " + b.tipo : "",
    b.quien ? "Solicitado por: " + b.quien : "",
    b.pedido ? "Fecha de solicitud: " + b.pedido : "",
    b.nota ? "Nota: " + b.nota : "",
    "(creada desde el portal de aprobaciones)",
  ].filter(Boolean).join("\n");
  await trelloPost("cards", {
    idList: list.id, name: String(b.titulo || "").slice(0, 160),
    desc, pos: "bottom", ...(lbl ? { idLabels: lbl.id } : {}),
  });
}

function uid() {
  return "x" + Math.random().toString(36).slice(2, 10) + Date.now().toString(36);
}
function find(arr, id) {
  return arr.find((x) => x.id === id);
}
function clip(s, n) {
  return String(s == null ? "" : s).slice(0, n);
}
function hoy() {
  const d = new Date(Date.now() - 4 * 3600 * 1000); // aprox Santiago
  return ("0" + d.getUTCDate()).slice(-2) + "-" + ("0" + (d.getUTCMonth() + 1)).slice(-2);
}
function log(x, texto) {
  x.history = x.history || [];
  x.history.push({ f: hoy(), t: clip(texto, 300) });
}

module.exports = async (req, res) => {
  if (req.method !== "POST") return res.status(405).json({ ok: false, error: "POST" });
  const b = req.body || {};
  const type = b.type;
  try {
    if (ADMIN.has(type) && !isPin(b.pin)) {
      return res.status(403).json({ ok: false, error: "pin" });
    }
    if (type === "ping") return res.status(200).json({ ok: true });

    // Con Trello activo, las solicitudes van directo al tablero (no al estado local).
    if (type === "queue_add" && trelloOn()) {
      if (!String(b.titulo || "").trim()) throw new Error("falta el título");
      await trelloQueueAdd(b);
      return res.status(200).json({ ok: true });
    }

    const at = await accessToken();
    const S = await readState(at);
    S.pieces = S.pieces || [];
    S.queue = S.queue || [];

    if (type === "approve") {
      const x = find(S.pieces, b.id); if (!x) throw new Error("pieza no existe");
      x.estado = "aprobada";
      log(x, "✔ Aprobada" + (b.autor ? " por " + clip(b.autor, 60) : "") + (x.v > 1 ? " (V" + x.v + ")" : ""));
    } else if (type === "reopen") {
      const x = find(S.pieces, b.id); if (!x) throw new Error("pieza no existe");
      x.estado = "pendiente";
      log(x, "Vuelta a pendiente");
    } else if (type === "comment") {
      const x = find(S.pieces, b.id); if (!x) throw new Error("pieza no existe");
      const texto = clip(b.texto, 2000).trim();
      if (!texto) throw new Error("comentario vacío");
      const autor = clip(b.autor, 60) || "Cliente";
      x.comments.push({ autor, fecha: clip(b.fecha, 10) || hoy(), texto, res: false });
      x.estado = "cambios";
      log(x, "✏ Cambios solicitados por " + autor);
    } else if (type === "piece_add") {
      const p = {
        id: uid(), marca: clip(b.marca, 4) || "DT", cat: clip(b.cat, 20) || "Grilla",
        titulo: clip(b.titulo, 160),
        formato: clip(b.formato, 40) || "Sin definir", fecha: clip(b.fecha, 60), copy: clip(b.copy, 2000),
        img: clip(b.img, 500) || null, v: 1, estado: "pendiente", comments: [], history: [],
      };
      log(p, "Pieza cargada (V1)");
      S.pieces.push(p);
    } else if (type === "piece_edit") {
      const x = find(S.pieces, b.id); if (!x) throw new Error("pieza no existe");
      if (b.titulo != null) x.titulo = clip(b.titulo, 160);
      if (b.fecha != null) x.fecha = clip(b.fecha, 60);
      if (b.copy != null) x.copy = clip(b.copy, 2000);
      if (b.cat != null) x.cat = clip(b.cat, 20) || x.cat;
    } else if (type === "piece_img") {
      const x = find(S.pieces, b.id); if (!x) throw new Error("pieza no existe");
      x.img = clip(b.img, 500);
      x.v = (x.v || 1) + 1;
      x.estado = "corregida";
      (x.comments || []).forEach((c) => { if (!c.res) { c.res = true; c.resEn = "V" + x.v; } });
      log(x, "🎨 Corrección subida: V" + x.v + (b.nota ? " — " + clip(b.nota, 200) : "") + ". Comentarios anteriores marcados resueltos.");
    } else if (type === "comment_resolve") {
      const x = find(S.pieces, b.id); if (!x) throw new Error("pieza no existe");
      const c = (x.comments || [])[b.idx];
      if (!c) throw new Error("comentario no existe");
      c.res = true; c.resEn = "V" + (x.v || 1);
      log(x, "Comentario marcado resuelto");
    } else if (type === "piece_fmt") {
      const x = find(S.pieces, b.id); if (!x) throw new Error("pieza no existe");
      x.formato = clip(b.formato, 40) || x.formato;
    } else if (type === "archivar") {
      // Archiva las aprobadas: salen de la vista activa pero la evidencia queda.
      S.archivo = S.archivo || [];
      const van = S.pieces.filter((p) => p.estado === "aprobada");
      if (!van.length) throw new Error("no hay piezas aprobadas para archivar");
      van.forEach((p) => { p.entrega = p.entrega || S.entrega; p.archivadaEl = hoy(); });
      S.archivo = van.concat(S.archivo).slice(0, 400);
      S.pieces = S.pieces.filter((p) => p.estado !== "aprobada");
    } else if (type === "piece_del") {
      S.pieces = S.pieces.filter((p) => p.id !== b.id);
    } else if (type === "queue_add") {
      S.queue.push({
        id: uid(), marca: clip(b.marca, 4) || "DT", titulo: clip(b.titulo, 160),
        tipo: clip(b.tipo, 60) || "Solicitud", pedido: clip(b.pedido, 10) || hoy(),
        quien: clip(b.quien, 60), estado: "cola", nota: clip(b.nota, 200),
      });
    } else if (type === "queue_move") {
      const i = S.queue.findIndex((q) => q.id === b.id);
      const j = b.dir === "up" ? i - 1 : i + 1;
      if (i >= 0 && j >= 0 && j < S.queue.length) {
        const t = S.queue[j]; S.queue[j] = S.queue[i]; S.queue[i] = t;
      }
    } else if (type === "queue_state") {
      const x = find(S.queue, b.id); if (!x) throw new Error("solicitud no existe");
      if (!["cola", "diseno", "revision", "entregada"].includes(b.estado)) throw new Error("estado inválido");
      x.estado = b.estado;
    } else if (type === "queue_del") {
      S.queue = S.queue.filter((q) => q.id !== b.id);
    } else if (type === "entrega") {
      S.entrega = clip(b.label, 80) || S.entrega;
    } else if (type === "clear") {
      S.archivo = S.archivo || [];
      const cerradas = S.pieces.filter((p) => p.estado === "aprobada");
      cerradas.forEach((p) => { p.entrega = p.entrega || S.entrega; p.archivadaEl = hoy(); });
      S.archivo = cerradas.concat(S.archivo).slice(0, 400);
      S.pieces = [];
    } else {
      throw new Error("acción desconocida");
    }

    await writeState(at, S);

    // Aviso automático al equipo en Slack cuando el cliente responde (opcional).
    if (process.env.SLACK_BOT_TOKEN && process.env.SLACK_CHANNEL && (type === "comment" || type === "approve")) {
      try {
        const x = find(S.pieces, b.id);
        const tag = x ? "[" + x.marca + (x.cat ? " · " + x.cat : "") + "] " + x.titulo : b.id;
        const msg = type === "approve"
          ? "🛎️ Portal Hilton — ✔ " + (b.autor || "Cliente") + " aprobó " + tag
          : "🛎️ Portal Hilton — ✏ " + (b.autor || "Cliente") + " pidió cambios en " + tag + ":\n«" + clip(b.texto, 500) + "»";
        await fetch("https://slack.com/api/chat.postMessage", {
          method: "POST",
          headers: { Authorization: `Bearer ${process.env.SLACK_BOT_TOKEN}`, "Content-Type": "application/json" },
          body: JSON.stringify({ channel: process.env.SLACK_CHANNEL, text: msg }),
        });
      } catch (e) { /* el aviso nunca bloquea la acción */ }
    }

    res.status(200).json({ ok: true, state: S });
  } catch (e) {
    res.status(400).json({ ok: false, error: String(e.message || e) });
  }
};
