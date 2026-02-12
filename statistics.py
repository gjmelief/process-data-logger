"""
statistics.py

Statistical calculations (average, min, max) for process sensor data.
Input: nested dict from read_log() in data_handler.py
"""

from data_handler import read_log

def calculate_average(sensor_data, sensor_name):
    """Calculate average for specific sensor.
    sensor_data = nested dict (output of read_log)
    sensor_name = e.g. "PI-001"
    """

    readings = list(sensor_data[sensor_name].values())
    average = round((sum(readings) / len(readings)), 1)
    return average

if __name__ == "__main__":
    sensor_data = read_log()
    print(calculate_average(sensor_data, "PI-001"))