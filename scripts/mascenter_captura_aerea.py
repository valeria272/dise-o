import asyncio, sys
from playwright.async_api import async_playwright

async def capturar(lat, lon, z, salida):
    async with async_playwright() as pw:
        nav = await pw.chromium.launch(channel="chrome", headless=True)
        pag = await nav.new_page(viewport={"width":1700,"height":1180}, device_scale_factor=2)
        await pag.goto(f"https://www.google.com/maps/@{lat},{lon},{z}z/data=!3m1!1e3?hl=es",
                       wait_until="domcontentloaded", timeout=60000)
        await pag.wait_for_timeout(11000)
        for t in ("Aceptar todo","Rechazar todo"):
            try:
                b=pag.get_by_role("button", name=t)
                if await b.count(): await b.first.click(timeout=2500); await pag.wait_for_timeout(4000)
            except Exception: pass

        # Apagar las etiquetas de Maps.
        # El conmutador NO es un <input>: es un <button role="checkbox"> de Google que
        # envuelve un <label> con el texto. Hacerle click al <label> no hace nada —
        # hay que subir al botón y verificar que aria-checked cambie a "false".
        estado = await pag.evaluate("""() => {
            const lab = [...document.querySelectorAll('label')]
                .find(l => ['Etiquetas','Labels'].includes(l.innerText.trim()));
            if (!lab) return 'sin control';
            const btn = lab.closest('button[role=checkbox]');
            if (!btn) return 'sin boton';
            if (btn.getAttribute('aria-checked') === 'true') btn.click();
            return btn.getAttribute('aria-checked');
        }""")
        await pag.wait_for_timeout(6000)
        print("etiquetas -> aria-checked:", estado)

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

asyncio.run(capturar(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
