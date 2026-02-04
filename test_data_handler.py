from pathlib import Path
import pytest
from data_handler import create_csv, pv_logger

def test_create_csv():
    """Test if create csv works as intended"""
    create_csv('test_process_data.csv')
    created_file = Path('test_process_data.csv')
    assert created_file.exists()
    created_file.unlink()

def test_pv_logger():
    """Test if pv_logger works as intended"""
    create_csv('test_process_data.csv')
    pv_logger('test_process_data.csv', '2026-02-03 18:00', 'PI-001', 26)
    created_file = Path('test_process_data.csv')
    content = created_file.read_text()
    assert "2026-02-03 18:00,PI-001,26" in content
    created_file.unlink()