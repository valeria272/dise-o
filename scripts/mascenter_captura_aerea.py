import asyncio, sys
from playwright.async_api import async_playwright

async def capturar(lat, lon, z, salida, dsf=2):
    async with async_playwright() as pw:
        nav = await pw.chromium.launch(channel="chrome", headless=True)
        pag = await nav.new_page(viewport={"width":1700,"height":1180}, device_scale_factor=float(dsf))
        await pag.goto(f"https://www.google.com/maps/@{lat},{lon},{z}z/data=!3m1!1e3?hl=es",
                       wait_until="domcontentloaded", timeout=60000)
        await pag.wait_for_timeout(11000)
        for t in ("Aceptar todo","Rechazar todo"):
            try:
                b=pag.get_by_role("button", name=t)
                if await b.count(): await b.first.click(timeout=2500); await pag.wait_for_timeout(4000)
            except Exception: pass

        # Apagar las etiquetas de Maps.
        # El conmutador NO es un <input>: es el <button role="checkbox"> que envuelve
        # al <label> con el texto. Y es intermitente — a veces el panel de capas aún
        # no está montado al primer intento, así que se verifica y se reintenta.
        estado = "sin control"
        for intento in range(6):
            estado = await pag.evaluate("""() => {
                const lab = [...document.querySelectorAll('label')]
                    .find(l => ['Etiquetas','Labels'].includes(l.innerText.trim()));
                if (!lab) return 'sin control';
                const btn = lab.closest('button[role=checkbox]');
                if (!btn) return 'sin boton';
                if (btn.getAttribute('aria-checked') === 'true') { btn.click(); return 'recien apagado'; }
                return 'apagado';
            }""")
            await pag.wait_for_timeout(3500)
            if estado == "apagado": break
        print(f"etiquetas: {estado} (intentos: {intento+1})")
        if estado != "apagado":
            raise RuntimeError("no se pudieron apagar las etiquetas — no sirve capturar así")
        await pag.wait_for_timeout(5000)

        await pag.add_style_tag(content="""
          #omnibox-container,#watermark,#runway-expand-button,.app-viewcard-strip,
          #vasquette,.scene-footer-container,#assistive-chips,#minimap,#gb,
          .widget-scene-footer,.app-bottom-content-anchor,#content-container,#titlecard,
          .searchbox,.widget-zoom,.watermark,.app-vertical-widget-holder,
          .app-horizontal-widget-holder,button { display:none !important; }
        """)
        await pag.wait_for_timeout(4000)
        await pag.screenshot(path=salida)
        await nav.close()
        print("capturado:", salida)

asyncio.run(capturar(*sys.argv[1:5], *(sys.argv[5:6])))
