from pathlib import Path

def create_csv(filename):
    """Create CSV file with header if it doesn't exist."""
    proc_data = Path(filename)

    if not proc_data.exists():
        proc_data.write_text('timestamp,tag,value\n')

def pv_logger(filename, timestamp, tag, value):
    """Write sensor reading to CSV file (long format).
    Check input validation against sensor specification"""

    error_message = f"Sensor {tag} is out of range.\nExiting the program."
    if 'PI' in tag:
        if value < -1 or value > 25:
            print(error_message)
            return

    if 'TI' in tag:
        if value < 0 or value > 380:
            print(error_message)
            return

    if 'FI' in tag:
        if value < 0 or value > 200:
            print(error_message)
            return

    proc_data = Path(filename)
    new_reading = f"{timestamp},{tag},{value}\n"
    with proc_data.open('a') as f:
        f.write(new_reading)

create_csv('process_data.csv')
pv_logger('process_data.csv', '2026-02-03 18:00', 'PI-001', 383)