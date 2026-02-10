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

def read_log(filename=DEFAULT_FILENAME):
    """Read the process data, convert to nested dict"""

    process_data_path = Path(filename)
    process_data_contents = process_data_path.read_text()
    readings = process_data_contents.splitlines()
    log = {}
    for reading in readings:
        # Split in timestamp, tag, value
        fields = reading.split(',')
        # If tag doesn't exist. Add to dict (outer layer)
        if fields[1] not in log:
            log[fields[1]] = {}
        # If tag exists. Add timestamp:value to inner dict
        log[fields[1]]['timestamp'] = fields[0]
        log[fields[1]]['value'] = fields[2]