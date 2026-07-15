from selectolax.parser import HTMLParser


def find_listing_candidates(html):

    tree = HTMLParser(html)

    cards = []

    for node in tree.css("*"):

        text = node.text(strip=True)

        if "$" in text and len(text) > 30:
            cards.append({
                "tag": node.tag,
                "text": text[:250]
            })

    return cards
