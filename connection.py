import sqlite3
import uuid


def create_tables():
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
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
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()


def insert_driver(carnet: str, nombre_completo: str, edad: int):
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
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


def insert_taxi(chapa: str, recorrido: int, nombre_completo: str):
    connection = sqlite3.connect("taxis_db.sqlite")
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT driver_id FROM drivers where nombre_completo like ?''', ('%' + nombre_completo + '%',))
        row = cursor.fetchone()
        if row[0]:
            sql = ''' INSERT INTO taxis(taxi_id,chapa,recorrido,driver_id) VALUES(?,?,?,?); '''
            cursor.execute(sql, (uuid_v4(), chapa, recorrido, row[0]))
            connection.commit()
            print("Taxi inserted successfully into taxis table")
            cursor.close()
        else:
            print('Driver not found :(')
    except sqlite3.Error as error:
        print(error)
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
        else:
            print('No drivers stored :(')
        cursor.close()
    except sqlite3.Error as error:
        print(error)
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
        else:
            print('No taxis stored with more than 200km :(')
        cursor.close()
    except sqlite3.Error as error:
        print(error)
    finally:
        if connection:
            connection.close()


def uuid_v4():
    return uuid.uuid4().hex
