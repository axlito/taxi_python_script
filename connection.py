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
    list = []
    try:
        cursor.execute('''SELECT * FROM drivers''')
        rows = cursor.fetchall()
        for row in rows:
            list.append(row)
        cursor.close()
        return list
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()



def show_drivers():
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT * FROM drivers''')
        rows = cursor.fetchall()
        if len(rows) > 0:
            for row in rows:
                print(f'> {row[2]}, DNI: {row[1]}, Edad: {row[3]}\n')
            cursor.close()
            return True
        else:
            return False
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
        cursor.execute('''SELECT * FROM taxis 
                        inner join drivers d on d.driver_id = taxis.driver_id 
                        where recorrido > 200 
                        ''')
        rows = cursor.fetchall()
        if len(rows) > 0:
            for row in rows:
                print(f'> {row[1]}, Recorrido: {row[2]}Km, Chofer: {row[6]}\n')
            cursor.close()
            return True
        else:
            return False
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def find_taxi_by_driver_name(nombre_completo: str):
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT driver_id FROM drivers where nombre_completo like ?''', ('%' + nombre_completo + '%',))
        row = cursor.fetchone()
        if row[0]:
            cursor.execute(''' Select chapa from taxis where driver_id = ?''', (row[0],))
            chapa = cursor.fetchone()
            print(f'Chapa => {chapa[0]}')
            cursor.close()
            return True
        else:
            return False
    except sqlite3.Error as error:
        print(error)
        return False
    finally:
        if connection:
            connection.close()


def update_driver_name_by_dni(dni: str, nombre_completo: str):
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute(''' UPDATE drivers SET nombre_completo = ? WHERE carnet = ?''', (nombre_completo, dni))
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
