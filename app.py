from fastapi import FastAPI
from scrapers.rentfaster import get_page
from scrapers.rentalsca import test as rentals_test

app = FastAPI(title="Apartment Hunter")


@app.get("/")
def root():
    return {"status": "online"}


@app.get("/search")
def search(city: str = "ab/edmonton"):
    return get_page(city)


@app.get("/rentalsca")
def rentalsca():
    return rentals_test()
