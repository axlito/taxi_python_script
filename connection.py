import sqlite3
import uuid

connection = sqlite3.connect("taxis_db.sqlite")


def create_tables():
    cursor = connection.cursor()
    drivers_table = """CREATE TABLE IF NOT EXISTS drivers (
                        driver_id TEXT PRIMARY KEY UNIQUE,
                        carnet TEXT NOT NULL,
                        nombre_completo TEXT NOT NULL UNIQUE,
                        edad INTEGER NOT NULL
                    );"""
    cursor.execute(drivers_table)
    taxis_table = """CREATE TABLE IF NOT EXISTS taxis (
                taxi_id TEXT PRIMARY KEY UNIQUE,
                chapa TEXT NOT NULL,
                recorrido INTEGER NOT NULL,
                driver_id TEXT UNIQUE,
                FOREIGN KEY (driver_id)
                    REFERENCES drivers (driver_id)
                    ON DELETE CASCADE
            );"""
    cursor.execute(taxis_table)
    cursor.close()


def insert_driver(carnet: str, nombre_completo: str, edad: int):
    try:
        cursor = connection.cursor()
        sql = ''' INSERT INTO drivers(driver_id,carnet,nombre_completo,edad) VALUES(?,?,?,?); '''
        cursor.execute(sql, (uuid_v4(), carnet, nombre_completo, edad))
        connection.commit()
        print("Driver inserted successfully into drivers table")
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()


def uuid_v4():
    return uuid.uuid4().hex
