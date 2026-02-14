"""
process_logger.py

Main program loop and menu for the Process Data Logger.
Coordinates data logging, viewing, and statistics via CLI.
"""
from data_handler import pv_logger, create_csv, read_log

if __name__ == "__main__":

    create_csv(filename="test_menu.csv")
    sensor_data = read_log(filename="test_menu.csv")

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