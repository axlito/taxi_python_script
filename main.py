from connection import create_tables, insert_driver, insert_taxi, get_drivers, show_taxis_with_more_than_200_km, find_taxi_by_driver_name, update_driver_name_by_dni
import os, platform


class color:
    RED    = '\33[91m'
    GRAY   = '\33[90m'
    BLUE   = '\33[94m'
    GREEN  = '\33[92m'
    WHITE  = '\33[97m'
    YELLOW = '\33[93m'


def clear():
    os_name = platform.system()
    if os_name == 'Linux':
        os.system('clear')
    elif os_name == 'Windows':
        os.system('cls')


def insert_driver_function():
    clear()
    print(color.BLUE + ' Adding new driver:')
    print(color.GRAY + '-----------------------------------------------------------------')
    dni = input(color.GRAY + ' Type the driver DNI: ' + color.YELLOW)
    if dni:
        name = input(color.GRAY + ' Type the driver name: ' + color.YELLOW)
        if name:
            last_name = input(color.GRAY + ' Type the driver last name: ' + color.YELLOW)
            if last_name:
                return insert_driver(carnet=dni, nombre=name, apellido=last_name)


def insert_taxi_function():
    clear()
    print(color.BLUE + ' Adding new taxi:')
    print(color.GRAY + '-----------------------------------------------------------------')
    plate = input(color.GRAY + ' Type the taxi plate: ' + color.YELLOW)
    if plate:
        model = input(color.GRAY + ' Type the taxi model: ' + color.YELLOW)
        if model:
            kilometers = input(color.GRAY + ' Type the taxi kilometers: ' + color.YELLOW)
            if kilometers:
                print(color.GRAY + ' Select a driver name:')
                drivers = get_drivers()
                value = 1
                for driver in drivers:
                    print(color.GREEN + '  ' + str(value) + '. ' + color.GRAY + driver[2] + ' ' + driver[3])
                    value = value + 1
                name = input(color.GRAY + '  Type the number corresponding to the taxi driver name: ' + color.YELLOW)
                if name:
                    pos = int(name) - 1
                    uuid = drivers[pos][0]
                    return insert_taxi(chapa=plate, modelo=model, km_recorrido=kilometers, driver=uuid)


def show_drivers_function():
    drivers = get_drivers()
    print(color.BLUE + ' Drivers list')
    print(color.GRAY + '-----------------------------------------------------------------')
    for driver in drivers:
        print(color.GREEN + ' DNI: ' + color.WHITE + driver[1] + color.GREEN + ' Full Name: ' + color.WHITE + driver[2] + ' ' + driver[3])

# ! Not Working
def show_taxis_200km_function():
    taxis = show_taxis_with_more_than_200_km()
    print(color.BLUE + ' Taxis with more than 200km list')
    print(color.GRAY + '-----------------------------------------------------------------')
    for taxi in taxis:
        print(color.GREEN + 'DNI: ' + color.WHITE + taxi)

# TODO
def find_taxi_by_driver_function():
    clear()
    print(color.BLUE + ' Find taxi by driver name:')
    print(color.GRAY + '-----------------------------------------------------------------')
    name = input(color.GRAY + ' Type the driver name: ' + color.YELLOW)
    if name:
        last_name = input(color.GRAY + ' Type the driver last name: ' + color.YELLOW)
        if last_name:
            if find_taxi_by_driver_name(name, last_name):
                taxi = find_taxi_by_driver_name(name, last_name)
                print(taxi)
                print(color.GREEN + ' Plate: ' + color.WHITE + taxi[1] + color.GREEN + ' Model: ' + color.WHITE + taxi[2] + color.GREEN + ' Kilometers: ' + color.WHITE + str(taxi[3]) + color.GREEN + ' Driver: ' + color.WHITE + name + ' ' + last_name)
                return True
            else:
                return False



def start_app():
    print(color.GRAY + '-----------------------------------------------------------------')
    print(color.GREEN + ' 1. ' + color.GRAY + 'Insert driver')
    print(color.GREEN + ' 2. ' + color.GRAY + 'Insert taxi')
    print(color.GREEN + ' 3. ' + color.GRAY + 'Show drivers')
    print(color.GREEN + ' 4. ' + color.GRAY + 'Show taxis with more than 200km')
    print(color.GREEN + ' 5. ' + color.GRAY + 'Find taxi by driver name')
    print(color.GREEN + ' 6. ' + color.GRAY + 'Update driver name by DNI')
    print(color.GRAY + '-----------------------------------------------------------------')

    prompt = input(color.GRAY + ' Type your option: ' + color.YELLOW)

    if prompt == '1':
        if insert_driver_function():
            clear()
            print(color.GREEN + ' DONE: Driver added successfully')
            start_app()
        else:
            clear()
            print(color.RED + ' ERROR: Something went wrong')
            start_app()
    elif prompt == '2':
        if insert_taxi_function():
            clear()
            print(color.GREEN + ' DONE: Taxi added succesfully')
            start_app()
        else:
            clear()
            print(color.RED + ' ERROR: The driver must not have any taxi')
            start_app()
    elif prompt == '3':
        clear()
        show_drivers_function()
        start_app()
    elif prompt == '4':
        show_taxis_200km_function()
    elif prompt == '5':
        if find_taxi_by_driver_function():
            clear()
            start_app()
        else:
            clear()
            print(color.RED + ' ERROR: The driver does not exist')
            start_app()
    elif prompt == '6':
        print(prompt)
    else:
        clear()
        print(color.RED + ' ERROR: Select a valid option')
        start_app()

if __name__ == '__main__':
    
    clear()

    if create_tables():
        start_app()
    else:
        print(color.RED + ' ERROR: Could not connect to database')

