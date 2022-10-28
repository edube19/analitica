from playwright.sync_api import Playwright, sync_playwright, expect
import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tripadvisor.com.pe/Hotels-g34439-Miami_Beach_Florida-Hotels.html")
    #time.sleep(3)
    page.locator("taplc_global_nav_0 > div.global-nav-links.global-nav-bottom.ui_tabs.is-hidden-mobile > div > div.message_container.ui_column.is-1").click()
    page.click("component_7 > div > button")
    time.sleep(3)
    #para quitar el calendario
    try:
        page.locator("BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e > div:nth-child(2) > div > div:nth-child(2) > div > div > div.ZxKNQ > div > div > div > div.rujDD.q.c > div:nth-child(1) > div.SWwwt.notranslate > div:nth-child(1) > div.rJYai.Vt.Z1.start.selected").click()
        page.locator("BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e > div:nth-child(2) > div > div:nth-child(2) > div > div > div.ZxKNQ > div > div > div > div.rujDD.q.c > div:nth-child(1) > div.SWwwt.notranslate > div:nth-child(2) > div:nth-child(1)").click()
        page.locator("body > div.KWdaU.Za.f.e > div:nth-child(2) > div > button").click()
        print("salio del calendario")
    except:
        page.locator("taplc_global_nav_0 > div.global-nav-links.global-nav-bottom.ui_tabs.is-hidden-mobile > div > div.message_container.ui_column.is-1").click()
        time.sleep(3)
        print('DEBIO CERRAR')
        #https://www.tripadvisor.com.pe/Hotels-g34439-oa90-Miami_Beach_Florida-Hotels.html
        #page.click("#TRIP_PLANNER")
        time.sleep(3)
        print("Completado")
        time.sleep(3)
        #boton mostrar todo
        #page.click("component_7 > div > button")
        time.sleep(3)
        print('presiono el boton')
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
#dia 6
##BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e > div:nth-child(2) > div > div:nth-child(2) > div > div > div.ZxKNQ > div > div > div > div.rujDD.q.c > div:nth-child(1) > div.SWwwt.notranslate > div:nth-child(1) > div.rJYai.Vt.Z1.start.selected
#dia 7
#BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e > div:nth-child(2) > div > div:nth-child(2) > div > div > div.ZxKNQ > div > div > div > div.rujDD.q.c > div:nth-child(1) > div.SWwwt.notranslate > div:nth-child(2) > div:nth-child(1)

#salir
#body > div.KWdaU.Za.f.e > div:nth-child(2) > div > button

