from playwright.sync_api import Playwright, sync_playwright
import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tripadvisor.com.pe/Hotels-g34439-Miami_Beach_Florida-Hotels.html",wait_until = 'networkidle')
    # page.click('#lithium-root > main > nav > div > div > div.fOydb.o > a.EJavG.c._S.JlIuS > span')
    #page.evaluate("document.querySelector('body > div.KWdaU.Za.f.e > div:nth-child(2)').remove()")
    page.click('#global-nav-hotels')
    # page.click("#lithium-root > main > div:nth-child(4) > div > div > div.lMwow.ZLOro > div.LeBBQ > div.dWEXi > div.wUpSI > div > div > button.bqhCp.u.z.ZIYzG.iMAUz")
    #page.keyboard.press('Escape')
    #page.keyboard.press('Escape')
    # page.reload()
    print('recargo la pagina')
    time.sleep(3)
    #page.click('lithium-root > main > div:nth-child(4) > div > div > div.lMwow.ZLOro > div.dErAM._Z.l._U > div.oOsqo._Z')
    print("Completado")
    #page.click('#lithium-root > main > div:nth-child(4) > div > div > div.zamsQ > div > div > div.LvzMf._T > div > div > div:nth-child(3) > span > span > span > div > div > div.yJIls.z.M0 > header > div > div > div > a > div')
    page.locator('#component_7 > div > button')
    time.sleep(5)
    page.click('#component_7 > div > button')

    time.sleep(5)
    print('hizo click')
    with page.expect_popup() as first:
        page.click("#property_7606777")
    page1 = first.value
    page1.reload()
    time.sleep(3)
    nombre = page1.inner_text('#HEADING')
    print(nombre)
    page1.click('#HEADING')
    page1.click('#HEADING')
    page1.click('#HEADING')
    page1.click('#HEADING')
    # page.keyboard.press('Escape')
    # page.keyboard.press('Escape')    

    """ nombre = page1.evaluate("document.querySelector('#HEADING').innerText")
    print(nombre)
    precio1 = page1.evaluate("document.querySelector('#component_4 > div > div.premium_offers_area.offers > div:nth-child(1) > div > div.ui_column.is-4.qnqtP.P.u > div > div.WXMFC.b').innerText")
    print('Expedia',precio1)
    precio2 = page1.evaluate("document.querySelector('#component_4 > div > div.premium_offers_area.offers > div:nth-child(2) > div > div.ui_column.is-4.qnqtP.P.u > div > div').innerText")
    print('Booking.com', precio2)
    precio3 = page1.evaluate("document.querySelector('#component_4 > div > div.premium_offers_area.offers > div:nth-child(3) > div > div.ui_column.is-4.qnqtP.P.u > div > div.msiXY.b.Wa').innerText")
    print('agoda',precio3)  """
    for i in range(3):
        i = i+1
        precio = page1.inner_text('#component_4 > div > div.premium_offers_area.offers > div:nth-child(1) > div > div.ui_column.is-4.qnqtP.P.u > div > div.WXMFC.b')
        print(precio)
with sync_playwright() as playwright:
    run(playwright)