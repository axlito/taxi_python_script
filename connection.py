import sqlite3

connection = sqlite3.connect("taxis_db.sqlite")


def create_tables():
    cursor = connection.cursor()

    taxis_table = """CREATE TABLE IF NOT EXISTS taxis (
                taxi_id GUID,
                chapa TEXT NOT NULL,
                recorrido INTEGER NOT NULL
            );"""

    drivers_table = """CREATE TABLE IF NOT EXISTS drivers (
                    driver_id GUID,
                    nombre_completo TEXT NOT NULL,
                    edad INTEGER NOT NULL
                );"""

    cursor.execute(taxis_table)
    cursor.execute(drivers_table)

    cursor.close()
