from pathlib import Path

def create_csv(filename):
    """Create CSV file with header if it doesn't exist."""
    proc_data = Path(filename)

    if not proc_data.exists():
        proc_data.write_text('timestamp,tag,value\n')

def pv_logger(filename, timestamp, tag, value):
    """Write sensor reading to CSV file (long format)."""
    proc_data = Path(filename)
    new_reading = f"{timestamp},{tag},{value}\n"
    with proc_data.open('a') as f:
        f.write(new_reading)

create_csv('process_data.csv')
pv_logger('process_data.csv', '2026-02-03 18:00', 'PI-001', 5)