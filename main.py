from connection import create_tables, insert_driver, insert_taxi, show_drivers, show_taxis_with_more_than_200_km, \
    find_taxi_by_driver_name, update_driver_name_by_dni
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
    print(color.GREEN + 'Adding new driver:')
    dni = input(color.GRAY + 'Type the driver DNI: ' + color.YELLOW)
    if dni:
        name = input(color.GRAY + 'Type the driver name: ' + color.YELLOW)
        if name:
            last_name = input(color.GRAY + 'Type the driver last name: ' + color.YELLOW)
            if last_name:
                return insert_driver(carnet=dni, nombre=name, apellido=last_name)


def start_app():
    print(color.GREEN + '1. ' + color.GRAY + 'Insert driver')
    print(color.GREEN + '2. ' + color.GRAY + 'Insert taxi')
    print(color.GREEN + '3. ' + color.GRAY + 'Show drivers')
    print(color.GREEN + '4. ' + color.GRAY + 'Show tais with more than 200km')
    print(color.GREEN + '5. ' + color.GRAY + 'Find taxi by driver name')
    print(color.GREEN + '6. ' + color.GRAY + 'Update driver name by DNI')
    print(color.GRAY + '-----------------------------------------------------------------')

    prompt = input(color.GRAY + ' Type your option: ' + color.YELLOW)

    if prompt == '1':
        if insert_driver_function():
            clear()
            print(color.GREEN + 'Driver added successfully')
            print(color.GRAY + '-----------------------------------------------------------------')
            start_app()
    elif prompt == '2':
        print(prompt)
    elif prompt == '3':
        print(prompt)
    elif prompt == '4':
        print(prompt)
    elif prompt == '5':
        print(prompt)
    elif prompt == '6':
        print(prompt)
    else:
        clear()
        print(color.RED + 'ERROR: Select a valid option')
        print(color.GRAY + '-----------------------------------------------------------------')
        start_app()

if __name__ == '__main__':
    
    clear()

    if create_tables():
        start_app()
    else:
        print(color.RED + 'ERROR: Could not connect to database')

