from pathlib import Path
from datetime import datetime
from sensor_config import range_validation

DEFAULT_FILENAME = 'process_data.csv'

def create_csv(filename=DEFAULT_FILENAME):
    """Create CSV file with header if it doesn't exist."""
    proc_data = Path(filename)

    if not proc_data.exists():
        proc_data.write_text('timestamp,tag,value\n')

def pv_logger(tag, value, filename=DEFAULT_FILENAME):
    """Write sensor reading to CSV file (long format).
    Check input validation against sensor specification"""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    range_error = f"Sensor {tag} is out of range.\nExiting the program."
    sensor_error = f"The sensor {tag} doesn't exist.\nExiting the program"
    sensor_type = tag.split('-')[0]

    try:
        min_value = range_validation[sensor_type]['min']
        max_value = range_validation[sensor_type]['max']

        if value < min_value or value > max_value:
            print(range_error)
            return
    except KeyError:
        print(sensor_error)
        return

    proc_data = Path(filename)
    new_reading = f"{timestamp},{tag},{value}\n"
    with proc_data.open('a') as f:
        f.write(new_reading)