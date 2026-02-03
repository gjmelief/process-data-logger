from pathlib import Path

def create_csv():
    """Create CSV file with header if it doesn't exist."""
    proc_data = Path('process_data.csv')

    if not proc_data.exists():
        proc_data.write_text('timestamp,tag,value\n')

def pv_logger(filename, timestamp, tag, value):
    """Write sensor reading to CSV file (long format)."""
    pass

create_csv()