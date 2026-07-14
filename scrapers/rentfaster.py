from playwright.sync_api import sync_playwright

def get_page(city="ab/edmonton"):
    url = f"https://www.rentfaster.ca/{city}/"

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox"]
        )

        page = browser.new_page(
            viewport={"width": 1400, "height": 900}
        )

        page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=120000
        )

        page.wait_for_timeout(5000)

        html = page.content()

        with open("rentfaster.html", "w", encoding="utf-8") as f:
            f.write(html)

        browser.close()

        return {
            "url": url,
            "html_length": len(html)
        }
