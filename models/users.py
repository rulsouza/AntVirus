import sqlite3

from database import get_db_connection


def criar_usuario(name, email, password_hash):
    """Insere um usuário. Retorna False se o e-mail já estiver cadastrado."""
    connection = get_db_connection()
    try:
        connection.execute(
            "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
            (name, email, password_hash),
        )
        connection.commit()
        return True
    except sqlite3.IntegrityError:
        # A coluna email é UNIQUE, então o SQLite recusa e-mails repetidos.
        return False
    finally:
        connection.close()


def buscar_usuario_por_email(email):
    connection = get_db_connection()
    try:
        return connection.execute(
            "SELECT * FROM users WHERE email = ?", (email,)
        ).fetchone()
    finally:
        connection.close()
