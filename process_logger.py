"""
process_logger.py

Main program loop and menu for the Process Data Logger.
Coordinates data logging, viewing, and statistics via CLI.
"""
from data_handler import pv_logger, create_csv

if __name__ == "__main__":

    create_csv(filename="test_menu.csv")

    while True:
        print('---Menu---')
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