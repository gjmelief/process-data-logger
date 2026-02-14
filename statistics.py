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

def calculate_min(sensor_data, sensor_name):
    """Calculate minimum for specific sensor"""

    readings = list(sensor_data[sensor_name].values())
    min_value = min(readings)
    return min_value

def calculate_max(sensor_data, sensor_name):
    """Calculate maximum for specific sensor"""

    readings = list(sensor_data[sensor_name].values())
    max_value = max(readings)
    return max_value


if __name__ == "__main__":
    sensor_data = read_log()
    print(calculate_average(sensor_data, "PI-001"))
    print(calculate_min(sensor_data, "PI-001"))
    print(calculate_max(sensor_data, "PI-001"))