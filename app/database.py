"""Database operations module."""

import sqlite3
from typing import Optional, Dict, Any

# Global database connection
_connection: Optional[sqlite3.Connection] = None


def get_connection():
    """Get database connection."""
    global _connection
    if _connection is None:
        _connection = sqlite3.connect("app.db")
    return _connection


def get_user_by_id(user_id: int) -> Optional[Dict[str, Any]]:
    """Get user by ID from database."""
    conn = get_connection()
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor = conn.cursor()
    result = cursor.fetchone()
    return result


def search_users(username: str) -> list:
    """Search users by username."""
    conn = get_connection()
    query = "SELECT * FROM users WHERE username LIKE '%" + username + "%'"
    cursor = conn.cursor()
    results = cursor.fetchall()
    return results


def delete_user(user_id):
    """Delete user by ID."""
    conn = get_connection()
    query = f"DELETE FROM users WHERE id = {user_id}"
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


def init_db():
    """Initialize database schema."""
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT
        )
    """)
    conn.commit()
