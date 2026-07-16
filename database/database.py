import sqlite3

DB_NAME = "apartments.db"


def connect():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS listings(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        title TEXT,
        price INTEGER,
        address TEXT,
        bedrooms REAL,
        bathrooms REAL,
        pets INTEGER,
        url TEXT UNIQUE,
        hash TEXT,
        first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_listing(listing):

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO listings(
        source,
        title,
        price,
        address,
        bedrooms,
        bathrooms,
        pets,
        url,
        hash
    )
    VALUES(?,?,?,?,?,?,?,?,?)
    """, (
        listing["source"],
        listing["title"],
        listing["price"],
        listing["address"],
        listing["bedrooms"],
        listing["bathrooms"],
        int(listing["pets"]),
        listing["url"],
        listing["hash"]
    ))

    conn.commit()
    conn.close()
