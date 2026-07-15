from selectolax.parser import HTMLParser


class Extractor:

    def __init__(self, html):
        self.tree = HTMLParser(html)

    def links(self):
        return [
            a.attributes.get("href")
            for a in self.tree.css("a")
            if a.attributes.get("href")
        ]

    def text(self):
        return self.tree.body.text(separator="\n")
