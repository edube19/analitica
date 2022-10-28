from playwright.sync_api import Playwright, sync_playwright
import time
from recursos import leer_puntuacion
from openpyxl import Workbook

from recursos import leer_puntuacion
def run(playwright: Playwright) -> None:
    book=Workbook()
    sheet= book.active
    #creando el excel
    sheet['A1'] = 'Nombre Hotel'
    sheet['B1'] = 'Precio Expedia'
    sheet['C1'] = 'Precio Booking'
    sheet['D1'] = 'Precio Agoda'
    sheet['E1'] = 'Puntuacion general'
    sheet['F1'] = 'Direccion'
    sheet['G1'] = 'Ubicacion'
    sheet['H1'] = 'Limpieza'
    sheet['I1'] = 'Servicio'
    sheet['J1'] = 'Calidad/Precio'

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.tripadvisor.com.pe/Hotels-g34439-Miami_Beach_Florida-Hotels.html")
    # page.click('#lithium-root > main > nav > div > div > div.fOydb.o > a.EJavG.c._S.JlIuS > span')
    #page.evaluate("document.querySelector('body > div.KWdaU.Za.f.e > div:nth-child(2)').remove()")
    page.click('#global-nav-hotels')
    # page.click("#lithium-root > main > div:nth-child(4) > div > div > div.lMwow.ZLOro > div.LeBBQ > div.dWEXi > div.wUpSI > div > div > button.bqhCp.u.z.ZIYzG.iMAUz")
    #page.keyboard.press('Escape')
    #page.keyboard.press('Escape')
    # page.reload()

    #time.sleep(3)
    #page.click('lithium-root > main > div:nth-child(4) > div > div > div.lMwow.ZLOro > div.dErAM._Z.l._U > div.oOsqo._Z')

    #page.click('#lithium-root > main > div:nth-child(4) > div > div > div.zamsQ > div > div > div.LvzMf._T > div > div > div:nth-child(3) > span > span > span > div > div > div.yJIls.z.M0 > header > div > div > div > a > div')
    page.locator('#component_7 > div > button')
    #time.sleep(5)
    page.click('#component_7 > div > button')

    #time.sleep(5)
    with page.expect_popup() as first:
        page.click("#property_7606777")
    page1 = first.value
    page1.reload()
    #time.sleep(3)
    nombre = page1.inner_text('#HEADING')
    print(nombre)
    sheet['A2'] = nombre
    page1.click('#HEADING')
    page1.click('#HEADING')
    page1.click('#HEADING')
    page1.click('#HEADING')
    # page.keyboard.press('Escape')
    # page.keyboard.press('Escape')    

    for i in range(3):
        i = i+1
        precio = page1.inner_text(f'#component_4 > div > div.premium_offers_area.offers > div:nth-child({i}) > div > div.ui_column.is-4.qnqtP.P.u > div > div.WXMFC.b')
        print(precio)
        j=i+1
        if (j==2):
            sheet[f'B2'] = precio
        elif(j==3):
            sheet[f'C2'] = precio
        else:
            sheet[f'D2'] = precio
        

    puntuacion = page1.inner_text('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1) > div.grdwI.P > span')
    print('PUNTUACION', puntuacion)
    sheet['E2'] = puntuacion

    direccion = page1.inner_text('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1) > span')
    print(direccion)
    sheet['F2'] = direccion

    #UBICACION
    esferas = page1.evaluate(('''()=>{
            var doc = document.querySelector('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1)').childNodes[2].childNodes[0].getAttribute('class');
            return doc}'''))
    print(esferas)
    valoracion = leer_puntuacion(esferas)
    print(valoracion)
    sheet['G2'] = valoracion

    #LIMPIEZA
    esferas = page1.evaluate(('''()=>{
            var doc = document.querySelector('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1)').childNodes[3].childNodes[0].getAttribute('class');
            return doc}'''))
    print(esferas)
    valoracion = leer_puntuacion(esferas)
    print(valoracion)
    sheet['H2'] = puntuacion

    #SERVICIO
    esferas = page1.evaluate(('''()=>{
            var doc = document.querySelector('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1)').childNodes[4].childNodes[0].getAttribute('class');
            return doc}'''))
    print(esferas)
    valoracion = leer_puntuacion(esferas)
    print(valoracion)
    sheet['I2'] = puntuacion

    #CALIDAD PRECIO
    esferas = page1.evaluate(('''()=>{
            var doc = document.querySelector('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1)').childNodes[5].childNodes[0].getAttribute('class');
            return doc}'''))
    print(esferas)
    valoracion = leer_puntuacion(esferas)
    print(valoracion)
    sheet['J2'] = puntuacion
    ruta_guardar = 'C:/Users/user/Desktop/TRABAJOS_UNI/excel/data.xlsx'
    book.save(ruta_guardar)
    book.close() 

with sync_playwright() as playwright:
    run(playwright)