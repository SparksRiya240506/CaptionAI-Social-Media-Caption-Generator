import sqlite3


def init_db():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT,
            platform TEXT,
            tone TEXT,
            captions TEXT,
            hashtags TEXT,
            ctas TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_history(
        description,
        platform,
        tone,
        captions,
        hashtags,
        ctas):

    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO history
        (
            description,
            platform,
            tone,
            captions,
            hashtags,
            ctas
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        description,
        platform,
        tone,
        captions,
        hashtags,
        ctas
    ))

    conn.commit()
    conn.close()


def get_history():
    conn = sqlite3.connect("history.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM history
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return rows