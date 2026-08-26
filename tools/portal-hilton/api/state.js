const { accessToken, readState, trelloOn, trelloBoard } = require("./_lib");

module.exports = async (req, res) => {
  try {
    const [state, trello] = await Promise.all([
      accessToken().then(readState),
      trelloOn() ? trelloBoard().catch(() => null) : Promise.resolve(null),
    ]);
    res.setHeader("Cache-Control", "no-store");
    res.status(200).json({ ok: true, state, trello });
  } catch (e) {
    res.status(500).json({ ok: false, error: String(e.message || e) });
  }
};
