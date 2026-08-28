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

        # Apagar las etiquetas. El conmutador vive en el panel de "Capas", que sólo
        # se despliega al pasar el mouse; se acciona por JS para no depender de eso.
        apagado = await pag.evaluate("""() => {
            const nodos = Array.from(document.querySelectorAll('button,label,div'));
            const et = nodos.find(e => {
                const t = (e.getAttribute('aria-label') || e.innerText || '').trim();
                return t === 'Etiquetas' || t === 'Labels';
            });
            if (!et) return false;
            et.click();
            return true;
        }""")
        await pag.wait_for_timeout(5000)
        print("etiquetas apagadas:", apagado)

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
