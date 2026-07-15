import re

PRICE_RE = re.compile(r"\$[\d,]+")


def extract_price(text):

    match = PRICE_RE.search(text)

    if not match:
        return None

    return int(match.group().replace("$", "").replace(",", ""))
