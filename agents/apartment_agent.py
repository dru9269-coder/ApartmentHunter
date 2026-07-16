from browser.browser import Browser
from browser.listings import find_listing_candidates
from browser.parser import extract_price
from database.database import save_listing


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

                listing = {
                    "source": url,
                    "title": card["text"][:60],
                    "price": price,
                    "address": "",
                    "bedrooms": None,
                    "bathrooms": None,
                    "pets": False,
                    "url": url,
                    "hash": str(hash(card["text"]))
                }

                save_listing(listing)

                results.append(listing)

            return results

        finally:
            self.browser.stop()
