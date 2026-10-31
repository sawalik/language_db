"""Language OS v1: SQLite storage for the vocab DB and study log."""
import sqlite3
from contextlib import contextmanager
from datetime import date
from pathlib import Path

DB_PATH = Path(__file__).parent / "language_os.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS vocab (
    id         INTEGER PRIMARY KEY,
    language   TEXT NOT NULL,
    word       TEXT NOT NULL,
    reading    TEXT DEFAULT '',
    meaning    TEXT NOT NULL,
    example    TEXT DEFAULT '',
    source     TEXT DEFAULT '',
    status     TEXT NOT NULL DEFAULT 'new' CHECK (status IN ('new', 'learning', 'known')),
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (language, word)
);

CREATE TABLE IF NOT EXISTS study_log (
    id       INTEGER PRIMARY KEY,
    day      TEXT NOT NULL,
    language TEXT NOT NULL,
    minutes  INTEGER NOT NULL CHECK (minutes > 0),
    activity TEXT NOT NULL,
    notes    TEXT DEFAULT ''
);
"""

STATUSES = ("new", "learning", "known")


@contextmanager
def connect(path=DB_PATH):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def add_word(language, word, meaning, reading="", example="", source="", path=DB_PATH):
    """Insert a word; returns False if (language, word) already exists."""
    with connect(path) as c:
        cur = c.execute(
            "INSERT OR IGNORE INTO vocab (language, word, reading, meaning, example, source) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (language, word.strip(), reading, meaning, example, source),
        )
        return cur.rowcount == 1


def set_status(vocab_id, status, path=DB_PATH):
    if status not in STATUSES:
        raise ValueError(f"status must be one of {STATUSES}")
    with connect(path) as c:
        c.execute("UPDATE vocab SET status = ? WHERE id = ?", (status, vocab_id))


def search_vocab(language=None, status=None, text="", path=DB_PATH):
    sql, args = "SELECT * FROM vocab WHERE 1=1", []
    if language:
        sql += " AND language = ?"
        args.append(language)
    if status:
        sql += " AND status = ?"
        args.append(status)
    if text:
        sql += " AND (word LIKE ? OR reading LIKE ? OR meaning LIKE ?)"
        args += [f"%{text}%"] * 3
    sql += " ORDER BY created_at DESC, id DESC"
    with connect(path) as c:
        return [dict(r) for r in c.execute(sql, args)]


def log_study(language, minutes, activity, notes="", day=None, path=DB_PATH):
    with connect(path) as c:
        c.execute(
            "INSERT INTO study_log (day, language, minutes, activity, notes) VALUES (?, ?, ?, ?, ?)",
            (day or date.today().isoformat(), language, minutes, activity, notes),
        )


def list_log(language=None, limit=100, path=DB_PATH):
    sql, args = "SELECT * FROM study_log", []
    if language:
        sql += " WHERE language = ?"
        args.append(language)
    sql += " ORDER BY day DESC, id DESC LIMIT ?"
    args.append(limit)
    with connect(path) as c:
        return [dict(r) for r in c.execute(sql, args)]


def minutes_per_day(language=None, path=DB_PATH):
    sql, args = "SELECT day, SUM(minutes) AS minutes FROM study_log", []
    if language:
        sql += " WHERE language = ?"
        args.append(language)
    sql += " GROUP BY day ORDER BY day"
    with connect(path) as c:
        return [dict(r) for r in c.execute(sql, args)]


def streak(path=DB_PATH):
    """Consecutive days studied, counting back from today (or yesterday)."""
    from datetime import timedelta

    with connect(path) as c:
        days = {r["day"] for r in c.execute("SELECT DISTINCT day FROM study_log")}
    d = date.today()
    if d.isoformat() not in days:
        d -= timedelta(days=1)
    n = 0
    while d.isoformat() in days:
        n += 1
        d -= timedelta(days=1)
    return n


def languages(path=DB_PATH):
    with connect(path) as c:
        rows = c.execute(
            "SELECT language FROM vocab UNION SELECT language FROM study_log ORDER BY 1"
        )
        return [r["language"] for r in rows]
