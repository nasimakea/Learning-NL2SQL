# database/db_connection.py

import sqlite3
from contextlib import contextmanager


DATABASE_NAME = "clinic.db"


@contextmanager
def get_db_connection():
    """
    Context manager for SQLite connection
    """
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row  # return dict-like rows
    try:
        yield conn
    finally:
        conn.close()