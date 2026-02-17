"""
process_logger.py

Main program loop and menu for the Process Data Logger.
Coordinates data logging, viewing, and statistics via CLI.
"""
from data_handler import pv_logger, create_csv, read_log
from statistics import calculate_average, calculate_min, calculate_max

def log_reading(sensor_data, filename):
    """
    Handles user input for logging a sensor reading.
    Input: Tag and process value from user.
    """
    sensor_name = get_valid_sensor(sensor_data, "\nWhat tag do you want to log a value for? ")

    try:
        value = float(input("\nWhat is the process value? "))
        pv_logger(sensor_name, value, filename=filename)
    except ValueError:
        print("\nInput must be a number in the format x.x.")

def view_readings(sensor_data):
    """
    Displays last N readings for a selected tag.
    Input: Tag and number of readings from user.
    """
    sensor_name = get_valid_sensor(sensor_data, "\nWhat tag do you want to view the "
                                   "data for? ")

    try:
        number = int(input("How many readings do you want to see? "))
        print(f"\nHere are the last {number} readings for tag {sensor_name}.\n")
        readings = list(sensor_data[sensor_name].items())
        for timestamp, value in readings[-number:]:
            print(f"{timestamp}: {value}")
    except ValueError:
        print("\nInput must be a whole number.")

def view_statistics(sensor_data):
    """
    Displays requested statistic for a selected tag.
    Input: Tag and statistic type (avg, min, max) from user.
    """
    sensor_name = get_valid_sensor(sensor_data, "\nWhat tag do you want to view the "
                                   "statistic for? ")
    menu_options = ['1', '2', '3']
    print("\nWhat statistic do you want to view?\n"
          "1. Average\n"
          "2. Minimum\n"
          "3. Maximum\n")
    option = input("Choose option from above: ")
    if option not in menu_options:
            print(f"\n{option} Is not in the menu."
                  "\nChoose one of the options from above.")
    if option == '1':
        average = calculate_average(sensor_data, sensor_name)
        print(f"\nAverage: {average}")
    if option == '2':
        minimum = calculate_min(sensor_data, sensor_name)
        print(f"\nMinimum: {minimum}")
    if option == '3':
        maximum = calculate_max(sensor_data, sensor_name)
        print(f"\nMaximum: {maximum}")

def check_sensor_name(sensor_data, sensor_name):
    """
    Checks if sensor_name exists in sensor_data.
    sensor_data: Dictionary with the sensor readings.
    sensor_name: Sensor name to check.
    """
    return sensor_name in sensor_data

def get_valid_sensor(sensor_data, prompt):
    """
    Prompts user for a sensor name until a valid one is given.
    sensor_data: Dictionary with sensor readings.
    prompt: Input message shown to user.
    Returns: Valid sensor_name string.
    """
    while True:
        sensor_name = input(prompt).upper()
        if check_sensor_name(sensor_data, sensor_name):
            return sensor_name
        print(f"\n{sensor_name} doesn't exist. Give an existing tag.")

if __name__ == "__main__":

    filename = "test_menu.csv"
    create_csv(filename=filename)
    sensor_data = read_log(filename=filename)
    menu_options = ['1', '2', '3', '4']

    while True:
        print('\n---Menu---')
        print("1. Log Data\n"
              "2. View Data\n"
              "3. View Statistics\n"
              "4. Exit the program")
        option = input("Choose option from above: ")
        if option not in menu_options:
            print(f"\n{option} Is not in the menu."
                  "\nChoose one of the options from above.")

        if option == '1':
            print("\n---Log Data menu---")
            keep_logging = True
            while keep_logging:
                log_reading(sensor_data, filename)
                while True:
                    cont = input("\nDo you want to log another reading? y/n: ").lower()
                    if cont in ["n", "no"]:
                        sensor_data = read_log(filename=filename)
                        keep_logging = False
                        break
                    elif cont in ["yes", "y"]:
                        break
                    else:
                        print("Please enter y or n")

        if option == '2':
            print("\n---View Data menu---")
            keep_logging = True
            while keep_logging:
                view_readings(sensor_data)
                while True:
                    cont = input("\nDo you want to view another reading? y/n: ").lower()
                    if cont in ["n", "no"]:
                        keep_logging = False
                        break
                    elif cont in ["yes", "y"]:
                        break
                    else:
                        print("Please enter y or n")

        if option == '3':
            print("\n---View Statistics menu---")
            keep_logging = True
            while keep_logging:
                view_statistics(sensor_data)
                while True:
                    cont = input("\nDo you want to view another statistic? y/n: ").lower()
                    if cont in ["n", "no"]:
                        keep_logging = False
                        break
                    elif cont in ["yes", "y"]:
                        break
                    else:
                        print("Please enter y or n")

        if option == '4':
            break