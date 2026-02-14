"""
process_logger.py

Main program loop and menu for the Process Data Logger.
Coordinates data logging, viewing, and statistics via CLI.
"""
from data_handler import pv_logger, create_csv, read_log

def log_reading(filename):
    """
    Handles user input for logging a sensor reading.
    Input: Tag and process value from user.
    """

def view_readings(sensor_data):
    """
    Displays last N readings for a selected tag.
    Input: Tag and number of readings from user.
    """

def view_statistics(sensor_data):
    """
    Displays requested statistic for a selected tag.
    Input: Tag and statistic type (avg, min, max) from user.
    """

if __name__ == "__main__":

    filename = "test_menu.csv"
    create_csv(filename=filename)
    sensor_data = read_log(filename=filename)

    while True:
        print('\n---Menu---')
        print("1. Log Data\n"
              "2. View Data\n"
              "3. View Statistics\n"
              "4. Exit the program")
        option = input("Choose option from above: ")
        if option == '4':
            break

        if option == '1':
            tag = input("What tag do you want to log a value for? ").upper()
            value = int(input("What is the process value? "))
            pv_logger(tag, value, filename="test_menu.csv")

        if option == '2':
            print("---View Data menu---")
            sensor_name = input("What tag do you want to view the data for? ").upper()
            number = int(input("How many readings do you want to see? "))
            print(f"\nHere are the last {number} readings for tag {sensor_name}.\n")
            # Print the data
            readings = list(sensor_data[sensor_name].items())
            for timestamp, value in readings[-number:]:
                print(f"{timestamp}: {value}")