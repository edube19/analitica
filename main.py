from playwright.sync_api import Playwright, sync_playwright
from recursos import leer_puntuacion
from openpyxl import Workbook
import time
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
    
    pagina_base = 'https://www.tripadvisor.com.pe'
    pagina_lista = ''
    
    #Creacion del contexto de la pag web
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #entrando a la pagina web
    page.goto("https://www.tripadvisor.com.pe/Hotels-g34439-Miami_Beach_Florida-Hotels.html", wait_until ='networkidle')
    
    page.click('#global-nav-hotels')
    
    #boton ver todo
    page.locator('#component_7 > div > button')
    page.click('#component_7 > div > button')


    
    """variable =page.evaluate(('''()=>{
        var doc = document.querySelector('#taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_ad_density_control_0 > div:nth-child(2) > div > div.meta_listing.ui_columns.large_thumbnail_mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div:nth-child(1) > div > div').childNodes[0].getAttribute('id');
        return doc}'''))
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAA',variable)"""
    
 
    fila_excel=2
    for k in range(2,37):
        if (k!=8 and k!=9 and k!=6 and k!=12 and k!=18 and k!=24 and k!=30):
            with context.expect_page() as new_page_info:
                pagina_lista = page.locator('#taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_ad_density_control_0 > div:nth-child(2) > div > div.meta_listing.ui_columns.large_thumbnail_mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div:nth-child(1) > div')
                #print(pagina_lista)
                #print(type(pagina_lista))
                str_pagina = str(pagina_lista)
                print(str_pagina)
                #print(type(str_pagina))
                comienzo = str_pagina.find("https")
                final = str_pagina.find(">")
                print(comienzo,final)
                direccion = str_pagina[comienzo:final-1]
                print(direccion)
                """pagina_lista = page.evaluate('''()=>{
                        var doc = document.querySelector("#taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_ad_density_control_0 > div:nth-child(2) > div > div.meta_listing.ui_columns.large_thumbnail_mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div:nth-child(1) > div").childNodes[0].childNodes[0].getAttribute('href');
                        return doc}''')
                print(pagina_lista)"""
                
                """with page.expect_popup() as first:
                    print(k)
                    page.click(f'"#taplc_hsx_hotel_list_lite_dusty_hotels_combined_sponsored_ad_density_control_0 > div:nth-child({k}) > div > div.meta_listing.ui_columns.large_thumbnail_mobile.nonen > div.ui_column.is-8.main_col.allowEllipsis > div:nth-child(1) > div").childNodes[0].childNodes[0]')
                """
                page.goto(direccion)
                #quitar calendario
                #page1 = first.value
                #page 1
                time.sleep(3)
                print('ENTRO')
            
            page1 = new_page_info.value
            
            page1.reload()
            #extrayendo el nombre
            nombre = page1.inner_text('#HEADING')
            #print(nombre)
            sheet[f'A{fila_excel}'] = nombre
            page1.click('#HEADING')
            for i in range(3):
                i = i+1
                precio = page1.inner_text(f'#component_4 > div > div.premium_offers_area.offers > div:nth-child({i}) > div > div.ui_column.is-4.qnqtP.P.u > div > div.WXMFC.b')
                print(precio)
                j=i+1
                if (j==2):
                    sheet[f'B{fila_excel}'] = precio
                elif(j==3):
                    sheet[f'C{fila_excel}'] = precio
                else:
                    sheet[f'D{fila_excel}'] = precio
                
            #PUNTUACION
            puntuacion = page1.inner_text('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1) > div.grdwI.P > span')
            print('PUNTUACION', puntuacion)
            sheet[f'E{fila_excel}'] = puntuacion

            direccion = page1.inner_text('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1) > span')
            print(direccion)
            sheet[f'F{fila_excel}'] = direccion

            #UBICACION
            esferas = page1.evaluate(('''()=>{
                    var doc = document.querySelector('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1)').childNodes[2].childNodes[0].getAttribute('class');
                    return doc}'''))
            print(esferas)
            valoracion = leer_puntuacion(esferas)
            print(valoracion)
            sheet[f'G{fila_excel}'] = valoracion

            #LIMPIEZA
            esferas = page1.evaluate(('''()=>{
                    var doc = document.querySelector('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1)').childNodes[3].childNodes[0].getAttribute('class');
                    return doc}'''))
            print(esferas)
            valoracion = leer_puntuacion(esferas)
            print(valoracion)
            sheet[f'H{fila_excel}'] = puntuacion

            #SERVICIO
            esferas = page1.evaluate(('''()=>{
                    var doc = document.querySelector('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1)').childNodes[4].childNodes[0].getAttribute('class');
                    return doc}'''))
            print(esferas)
            valoracion = leer_puntuacion(esferas)
            print(valoracion)
            sheet[f'I{fila_excel}'] = puntuacion

            #CALIDAD PRECIO
            esferas = page1.evaluate('''()=>{
                    var doc = document.querySelector('#ABOUT_TAB > div.ui_columns.MXlSZ > div:nth-child(1)').childNodes[5].childNodes[0].getAttribute('class');
                    return doc}''')
            print(esferas)
            valoracion = leer_puntuacion(esferas)
            print(valoracion)
            sheet[f'J{fila_excel}'] = puntuacion
            
            page1.close()
            fila_excel=fila_excel+1
        print(k)
    ruta_guardar = 'C:/Users/PCB/Desktop/analitica-main/data.xlsx'
    book.save(ruta_guardar)
    book.close() 

with sync_playwright() as playwright:
    run(playwright)