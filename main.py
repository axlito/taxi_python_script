from connection import create_tables, insert_driver, insert_taxi, show_drivers, show_taxis_with_more_than_200_km, \
    find_taxi_by_driver_name, update_driver_name_by_dni

if __name__ == '__main__':
    create_tables()
    # insert_driver('97122558711', 'Cristhiam Lopez', 25)
    # insert_taxi('P987456', 250, 'Cristhiam')
    # show_drivers()
    # show_taxis_with_more_than_200_km()
    # find_taxi_by_driver_name('Yohan')
    # update_driver_name_by_dni('97100908262', 'Zahiri Nat Zuke')
