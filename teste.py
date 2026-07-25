# Imports
import asyncio
from playwright.async_api import async_playwright
import time
from loader import scroll_to_bottom
from config import *


URL = "https://www.google.com/maps/search/restaurantes+em+cotia/@-23.6052876,-46.9895799,12z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI2MDcyMS4wIKXMDSoASAFQAw%3D%3D"
async def scrapper(query):

    async with async_playwright() as p:

        # Dictionary to store the results
        results = {'card_results': [], 'card_url': [], 'card_plus_code': []}

        URL = Config.url + query.replace(" ", "+")  # Constructing the URL based on the query

        browser = await p.chromium.launch(headless=Config.headless)  # Launching the browser in headless mode based on config
        context = await browser.new_context(locale="en-US") # Defining the locale
        page = await context.new_page()
        await page.goto(URL, wait_until="domcontentloaded")
        await page.wait_for_timeout(5000)

        await scroll_to_bottom(page)      # Scroll to the bottom of the page

        cards = page.locator('[role="article" ]')

        for i in range(Config.card_limit):    # Testing the first 10 cards
 
            print(f"\n========== CARD {i+1} ==========")

            # Recreating the card locator for each iteration to avoid stale element reference errors
            card = page.locator('[role="article"]').nth(i)

            try:

                name = await card.text_content(timeout=3000)
                print(f"Name:\n{name[:80]}")
        
                await card.click(timeout=7000)
                await page.wait_for_timeout(4500)

                # Plus Code
                plus_code = await page.locator('button[data-item-id^="oloc"]').text_content(timeout=2000)
                print("Plus Code:", plus_code)

                # Card link Extraction    
                link = await card.locator("a").first.get_attribute("href")
                print("Link:", link)

            except Exception as e:

                print("Erro:", e)

            await asyncio.sleep(2)

        await browser.close()

        return results

results = asyncio.run(scrapper("restaurantes em cotia"))