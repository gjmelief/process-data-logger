import pytest
from data_handler import create_csv, read_log
from statistics import calculate_average, calculate_min, calculate_max


def test_calculate_average():
    """Test if average is calculated correctly"""
    sensor_data = read_log(filename='test_process_data.csv')
    average = calculate_average(sensor_data, "PI-001")
    assert average == 2.2

def test_calculate_min():
    """Test if minium is calculated correctly"""
    sensor_data = read_log(filename='test_process_data.csv')
    min_value = calculate_min(sensor_data, "PI-001")
    assert min_value == 2.1

def test_calculate_max():
    """Test if maximum is calculated correctly"""
    sensor_data = read_log(filename='test_process_data.csv')
    max_value = calculate_max(sensor_data, "PI-001")
    assert max_value == 2.4