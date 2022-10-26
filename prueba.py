from playwright.sync_api import Playwright, sync_playwright, expect
import time
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tripadvisor.com.pe/Hotels-g34439-Miami_Beach_Florida-Hotels.html")
    time.sleep(3)
    page.click("#TRIP_PLANNER")
    with context.expect_page() as new_page_info:
        page.locator('#property_7606777').click() # Opens a new tab
    new_page = new_page_info.value

    new_page.wait_for_load_state()
    page.locator("#MAIN").click()
    time.sleep(3)
    nombre = new_page.inner_text("document.querySelector('#HEADING')")
    print(nombre)
    #page.click('#property_7606777')
    time.sleep(3)
    print("Completado")
    """
    page1.locator("#component_14").get_by_text("N.º 6 de 230 hoteles en Miami Beach").click()
    page1.get_by_text("Estación de carga eléctrica para vehículos").click()
    page1.get_by_text("Internet de alta velocidad gratuito (WiFi)").click()
    page1.get_by_text("Gimnasio / Sala de entrenamiento").click()
    page1.locator("#component_14").get_by_text("Bar/Salón").click()
    page1.locator("#component_14").get_by_text("Playa").first.click()
    page1.get_by_text("Bicicletas disponibles").click()
    page1.get_by_text("Guardería").click()
    page1.close()"""
    
    """time.sleep(3)
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="2. Mondrian South Beach Hotel").click()
    page2 = popup_info.value
    page.wait_for_url("https://www.tripadvisor.com.pe/Hotel_Review-g34439-d1163622-Reviews-Mondrian_South_Beach_Hotel-Miami_Beach_Florida.html")
    page2.get_by_role("heading", name="Mondrian South Beach Hotel").click()
    page2.get_by_text("4.5").click()
    page2.locator("#component_14").get_by_text("N.º 15 de 230 hoteles en Miami Beach").click()
    page2.get_by_text("Estación de carga eléctrica para vehículos").click()
    page2.get_by_text("Internet de alta velocidad gratuito (WiFi)").click()
    page2.locator(".OsCbb > div:nth-child(3)").first.click()
    page2.get_by_text("Gimnasio / Sala de entrenamiento").click()
    page2.locator("#component_14").get_by_text("Bar/Salón").click()
    page2.get_by_text("Bicicletas disponibles").click()
    page2.get_by_text("Se admiten mascotas (Se aceptan perros / mascotas)").click()
    page2.get_by_text("Transporte al aeropuerto").click()
    page2.close()
    time.sleep(3)
    print("Completado")
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="3. The Goodtime Hotel").click()
    page3 = popup_info.value
    page.wait_for_url("https://www.tripadvisor.com.pe/Hotel_Review-g34439-d23093311-Reviews-The_Goodtime_Hotel-Miami_Beach_Florida.html")
    page3.get_by_role("heading", name="The Goodtime Hotel").click()
    page3.get_by_text("5.0").click()
    page3.locator("#component_14").get_by_text("N.º 4 de 230 hoteles en Miami Beach").click()
    page3.get_by_text("Estacionamiento con servicio de valet").click()
    page3.get_by_text("Internet de alta velocidad gratuito (WiFi)").click()
    page3.locator("#component_14").get_by_text("Piscina").first.click()
    page3.get_by_text("Gimnasio / Sala de entrenamiento").click()
    page3.get_by_text("Alquiler de bicicletas").click()
    page3.locator("#component_14").get_by_text("Bar/Salón").click()
    page3.get_by_text("Bicicletas disponibles").click()
    page3.get_by_text("Centro de negocios con acceso a Internet").click()
    page3.close()
    time.sleep(3)
    print("Completado")"""
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)