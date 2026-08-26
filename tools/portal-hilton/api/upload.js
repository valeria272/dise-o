const { accessToken, isPin, carpetaDestino } = require("./_lib");

// Sube una imagen (data URI JPEG/PNG ya comprimida por el navegador) a la carpeta
// del portal en Drive, la hace pública por enlace y devuelve la URL directa.
module.exports = async (req, res) => {
  if (req.method !== "POST") return res.status(405).json({ ok: false, error: "POST" });
  const b = req.body || {};
  if (!isPin(b.pin)) return res.status(403).json({ ok: false, error: "pin" });
  try {
    const m = /^data:(image\/(?:jpeg|png|webp)|application\/pdf);base64,(.+)$/.exec(b.dataUri || "");
    if (!m) throw new Error("archivo inválido (solo imagen o PDF)");
    const mime = m[1];
    const buf = Buffer.from(m[2], "base64");
    if (buf.length > 4 * 1024 * 1024) throw new Error("el archivo pesa más de 4 MB");

    const at = await accessToken();
    const carpeta = await carpetaDestino(at, { entrega: b.entrega, marca: b.marca, cat: b.cat });
    const base = String(b.name || "pieza").replace(/[^\w.\-]+/g, "_").slice(0, 80) || "pieza";
    const ext = mime === "application/pdf" ? ".pdf" : (mime === "image/png" ? ".png" : ".jpg");
    const name = base + "_" + Date.now() + ext;
    const meta = JSON.stringify({ name, parents: [carpeta] });
    const boundary = "b" + Math.random().toString(36).slice(2);
    const body = Buffer.concat([
      Buffer.from(`--${boundary}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n${meta}\r\n--${boundary}\r\nContent-Type: ${mime}\r\n\r\n`),
      buf,
      Buffer.from(`\r\n--${boundary}--`),
    ]);
    const up = await fetch("https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart&fields=id", {
      method: "POST",
      headers: { Authorization: `Bearer ${at}`, "Content-Type": `multipart/related; boundary=${boundary}` },
      body,
    });
    if (!up.ok) throw new Error("drive upload " + up.status);
    const id = (await up.json()).id;

    const perm = await fetch(`https://www.googleapis.com/drive/v3/files/${id}/permissions`, {
      method: "POST",
      headers: { Authorization: `Bearer ${at}`, "Content-Type": "application/json" },
      body: JSON.stringify({ role: "reader", type: "anyone" }),
    });
    if (!perm.ok) throw new Error("drive perm " + perm.status);

    const esPdf = mime === "application/pdf";
    res.status(200).json({
      ok: true,
      kind: esPdf ? "pdf" : "img",
      fileId: id,
      folderId: carpeta,
      url: esPdf ? `https://drive.google.com/file/d/${id}/preview` : `https://lh3.googleusercontent.com/d/${id}`,
    });
  } catch (e) {
    res.status(400).json({ ok: false, error: String(e.message || e) });
  }
};
