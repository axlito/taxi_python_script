import sqlite3
import uuid


def create_tables():
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        drivers_table = """CREATE TABLE IF NOT EXISTS drivers (
                            driver_id TEXT PRIMARY KEY UNIQUE,
                            carnet TEXT NOT NULL,
                            nombre TEXT NOT NULL,
                            apellido TEXT NOT NULL
                        );"""
        cursor.execute(drivers_table)
        taxis_table = """CREATE TABLE IF NOT EXISTS taxis (
                    taxi_id TEXT PRIMARY KEY UNIQUE,
                    chapa TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    km_recorrido INTEGER NOT NULL,
                    driver_id TEXT UNIQUE,
                    FOREIGN KEY (driver_id)
                        REFERENCES drivers (driver_id)
                        ON DELETE CASCADE
                );"""
        cursor.execute(taxis_table)
        cursor.close()
        return True
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def insert_driver(carnet: str, nombre: str, apellido:str):
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        sql = ''' INSERT INTO drivers(driver_id, carnet, nombre, apellido) VALUES(?,?,?,?); '''
        cursor.execute(sql, (uuid_v4(), carnet, nombre, apellido))
        connection.commit()
        cursor.close()
        return True
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def insert_taxi(chapa: str, modelo:str, km_recorrido:int, driver:str):
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        sql = ''' INSERT INTO taxis(taxi_id, chapa, modelo, km_recorrido, driver_id) VALUES(?,?,?,?,?); '''
        cursor.execute(sql, (uuid_v4(), chapa, modelo, km_recorrido, driver))
        connection.commit()
        cursor.close()
        return True
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def get_drivers():
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT * FROM drivers''')
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def show_taxis_with_more_than_200_km():
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT * FROM taxis where km_recorrido > 200''')
        rows = cursor.fetchall()
        cursor.close()
        return rows
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()

# TODO Inner Join
def find_taxi_by_driver_name(nombre: str, apellido: str):
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT driver_id FROM drivers where nombre like ? or apellido like ?''', ('%' + nombre + '%', '%' + apellido + '%'))
        row = cursor.fetchone()
        if row is not None:
            cursor.execute('''Select * from taxis where driver_id = ?''', (row[0],))
            taxi = cursor.fetchone()
            cursor.close()
            return taxi
        else:
            return False
    except sqlite3.Error as error:
        return False
    finally:
        if connection:
            connection.close()

# TODO Fix Error Handling
def update_driver_name_by_dni(dni: str, nombre: str, apellido: str):
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute(''' UPDATE drivers SET nombre = ?, apellido = ? WHERE carnet = ?''', (nombre, apellido, dni))
        connection.commit()
        cursor.close()
        return True
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def uuid_v4():
    return uuid.uuid4().hex
