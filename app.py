from fastapi import FastAPI, Query
from scrapers.rentfaster import get_page
from scrapers.rentalsca import test as rentals_test
from agents.apartment_agent import ApartmentAgent
import sqlite3


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


@app.get("/agent")
def agent(url: str = Query(...)):

    a = ApartmentAgent()

    return a.search(url)


@app.get("/listings")
def listings():

    conn = sqlite3.connect("apartments.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM listings
        ORDER BY first_seen DESC
    """)

    rows = [dict(r) for r in cur.fetchall()]

    conn.close()

    return rows
