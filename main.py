from playwright.sync_api import Playwright, sync_playwright
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)
    page = context.new_page()
    i=0
    while i<10:
        print(i)
        page.goto("https://www.tripadvisor.com.pe/Hotels-g34439-Miami_Beach_Florida-Hotels.html")
        page.click("#property_7606777")
        i +=1
    

with sync_playwright() as playwright:
    run(playwright)