from playwright.sync_api import Playwright, sync_playwright
import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tripadvisor.com.pe/Hotels-g34439-Miami_Beach_Florida-Hotels.html")

    print('entro')
    page.evaluate(('''()=>{
            "document.querySelector('BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e').remove()"    
            }'''))
    #page.evaluate("document.querySelector('BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e').remove()")
    time.sleep(3)
    #BODY_BLOCK_JQUERY_REFLOW > div.KWdaU.Za.f.e
    """page.locator("taplc_global_nav_onpage_assets_0 > div > div").click()
    page.locator("taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_ad_density_control_0").click()"""
    print('paso la tabla')
    context.close()
    browser.close()
    #TABLA
    #taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_ad_density_control_0
with sync_playwright() as playwright:
    run(playwright)