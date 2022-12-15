from connection import create_tables, insert_driver, insert_taxi, show_drivers, show_taxis_with_more_than_200_km, \
    find_taxi_by_driver_name, update_driver_name_by_dni
import os, platform

def clear():
    os_name = platform.system()
    if os_name == 'Linux':
        os.system('clear')
        # print('Linux')
    elif os_name == 'Windows':
        os.system('cls')
        # print('Windows')

def start_app():
    print('1. Insert driver')
    print('2. Insert taxi')
    print('3. Show drivers')
    print('4. Show tais with more than 200km')
    print('5. Find taxy by driver name')
    print('6. Update driver name by DNI')

    prompt = input('Type your option: ')
    if prompt == '1':
        print(prompt)
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
        print('ERROR: Select a valid option')
        print('-----------------------------------------------------------------')
        start_app()

if __name__ == '__main__':
    clear()
    create_tables()
    start_app()
