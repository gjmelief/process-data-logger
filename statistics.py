"""
statistics.py

Statistical calculations (average, min, max) for process sensor data.
Input: nested dict from read_log() in data_handler.py
"""

from data_handler import read_log

def calculate_average(sensor_data, sensor_name):
    """Calculate average for specific sensor.
    sensor_data = nested dict (output van read_log)
    sensor_name = e.g. "PI-001"
    """