from pathlib import Path

def create_csv():
    """Create CSV file with header if it doesn't exist."""
    proc_data = Path('process_data.csv')

    if proc_data.exists():
        print('bestaat')
    else:
        proc_data.write_text('timestamp,tag,value')


def pv_logger(filename, timestamp, tag, value):
    """Write sensor reading to CSV file (long format)."""
    pass

create_csv()