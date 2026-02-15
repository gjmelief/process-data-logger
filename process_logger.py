"""
process_logger.py

Main program loop and menu for the Process Data Logger.
Coordinates data logging, viewing, and statistics via CLI.
"""
from data_handler import pv_logger, create_csv, read_log
from statistics import calculate_average, calculate_min, calculate_max

def log_reading(filename):
    """
    Handles user input for logging a sensor reading.
    Input: Tag and process value from user.
    """
    tag = input("What tag do you want to log a value for? ").upper()
    value = int(input("What is the process value? "))
    pv_logger(tag, value, filename=filename)

def view_readings(sensor_data):
    """
    Displays last N readings for a selected tag.
    Input: Tag and number of readings from user.
    """
    sensor_name = input("What tag do you want to view the data for? ").upper()
    number = int(input("How many readings do you want to see? "))
    print(f"\nHere are the last {number} readings for tag {sensor_name}.\n")
    readings = list(sensor_data[sensor_name].items())
    for timestamp, value in readings[-number:]:
        print(f"{timestamp}: {value}")

def view_statistics(sensor_data):
    """
    Displays requested statistic for a selected tag.
    Input: Tag and statistic type (avg, min, max) from user.
    """
    sensor_name = input("What tag do you want to view the statistic for? ").upper()
    print("\nWhat statistic do you want to view?\n"
          "1. Average\n"
          "2. Minimum\n"
          "3. Maximum\n")
    option = input("Choose option from above: ")
    if option == '1':
        average = calculate_average(sensor_data, sensor_name)
        print(f"\nAverage: {average}")
    if option == '2':
        minimum = calculate_min(sensor_data, sensor_name)
        print(f"\nMinimum: {minimum}")
    if option == '3':
        maximum = calculate_max(sensor_data, sensor_name)
        print(f"\nMaximum: {maximum}")

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
                  "\nChoose one of the options above")

        if option == '1':
            print("\n---Log Data menu---")
            while True:
                log_reading(filename)
                cont = input("\nDo you want to log another reading? y/n: ").lower()
                if cont == "n":
                    sensor_data = read_log(filename=filename)
                    break

        if option == '2':
            print("\n---View Data menu---")
            while True:
                view_readings(sensor_data)
                cont = input("\nDo you want to view another reading? y/n: ").lower()
                if cont == "n":
                    break

        if option == '3':
            print("\n---View Statistics menu---")
            while True:
                view_statistics(sensor_data)
                cont = input("\nDo you want to view another statistic? y/n: ").lower()
                if cont == "n":
                    break

        if option == '4':
            break