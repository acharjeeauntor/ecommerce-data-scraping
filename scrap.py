from playwright.async_api import async_playwright
import json

URL = "https://www.bestbuy.ca/en-ca/product/jbl-xtreme-2-rugged-waterproof-bluetooth-wireless-speaker-black/12568005"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(URL)
        await page.wait_for_load_state("load")
        
        title = await page.locator("section div h1").text_content()
        image_URL = await page.locator('[data-automation="image-slider-test"] img').nth(0).get_attribute("src")
        description = await page.locator(".description_1N8uX").text_content()
        data = {
            "title": title,
            "image_URL": image_URL,
            "description": description
        }

        with open("data.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        await browser.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
