import requests

def test():
    url = "https://rentals.ca/edmonton"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/137.0.0.0 Safari/537.36"
        )
    }

    r = requests.get(url, headers=headers, timeout=30)

    with open("rentalsca.html", "w", encoding="utf-8") as f:
        f.write(r.text)

    return {
        "status": r.status_code,
        "length": len(r.text)
    }
