from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright
import asyncio


async def main():
    async with async_playwright() as p:
        #construct browser environment
        browser = await p.webkit.launch()
        page = await browser.new_page()

        #go to url of blazor site
        await page.goto("http://localhost:5000/")

        #screenshot
        await page.screenshot(path="main.png")
        print("sd")
        await page.goto("http://localhost:5000/counter")
        print("sdf")
        await page.screenshot(path="counter.png")
        print("sdf")

        #click button
        await page.click("text=Click me")
        await page.click("text=Click me")
        await page.click("text=Click me")
        await page.click("text=Click me")
        print("sdf")
        await page.screenshot(path="counter2.png")
        print("p?")
        a = await page.get_attribute("id=num", "text")
        print(a, type(a))
        await browser.close()

asyncio.run(main())



