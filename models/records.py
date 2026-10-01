from database import get_db_connection


def listar_registros():
    connection = get_db_connection()
    try:
        return connection.execute(
            "SELECT * FROM records ORDER BY created_at DESC"
        ).fetchall()
    finally:
        connection.close()


def buscar_registro(record_id):
    connection = get_db_connection()
    try:
        return connection.execute(
            "SELECT * FROM records WHERE id = ?", (record_id,)
        ).fetchone()
    finally:
        connection.close()


def criar_registro(title, description):
    connection = get_db_connection()
    try:
        connection.execute(
            "INSERT INTO records (title, description) VALUES (?, ?)",
            (title, description),
        )
        connection.commit()
    finally:
        connection.close()


def atualizar_registro(record_id, title, description):
    connection = get_db_connection()
    try:
        # UPDATE altera dados que já existem no banco.
        connection.execute(
            "UPDATE records SET title = ?, description = ? WHERE id = ?",
            (title, description, record_id),
        )
        connection.commit()
    finally:
        connection.close()


def excluir_registro(record_id):
    connection = get_db_connection()
    try:
        connection.execute("DELETE FROM records WHERE id = ?", (record_id,))
        connection.commit()
    finally:
        connection.close()
