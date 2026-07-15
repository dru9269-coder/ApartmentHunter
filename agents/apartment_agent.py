from browser.browser import Browser
from browser.listings import find_listing_candidates
from browser.parser import extract_price


class ApartmentAgent:

    def __init__(self):
        self.browser = Browser()

    def search(self, url):

        self.browser.start()

        try:
            page = self.browser.get_page(url)

            cards = find_listing_candidates(page.content())

            results = []

            for card in cards:

                price = extract_price(card["text"])

                results.append({
                    "price": price,
                    "preview": card["text"][:150]
                })

            return results

        finally:
            self.browser.stop()
