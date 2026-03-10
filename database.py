import sqlite3
from datetime import datetime

from weather import get_weather

def get_connection():
    conn = sqlite3.connect("morning_feed.db")
    conn.row_factory = sqlite3.Row # allows us to access columns by name
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temp REAL,
            feels_like REAL,
            description TEXT,
            humidity INTEGER,
            fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        title TEXT,
        description TEXT,
        url TEXT,
        published_at TEXT,
        fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bias_analysis(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        analysis TEXT,
        fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
    
    conn.commit()
    conn.close()
    print ("Database initialized successfully.")

def save_weather(weather_data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO weather (city, temp, feels_like, description, humidity)
        VALUES (?, ?, ?, ?, ?)
    """, (
        weather_data["city"],
        weather_data["temp"],
        weather_data["feels_like"],
        weather_data["description"],
        weather_data["humidity"]
    ))

    conn.commit()
    conn.close()


def save_articles(articles):
    conn = get_connection()
    cursor = conn.cursor()
    for article in articles:
        cursor.execute("""
            INSERT INTO articles (source, title, description, url, published_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            article["source"],
            article["title"],
            article["description"],
            article["url"],
            article.get("published_at", "")
        ))

    conn.commit()
    conn.close()

def save_analysis(content):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bias_analysis (analysis)
        VALUES (?)
    """, (content,))

    conn.commit()
    conn.close()

