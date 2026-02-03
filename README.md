# Process Data Logger

CLI tool that simulates process data logging in a manufacturing environment. Logs sensor readings (pressure, temperature, flow) to CSV with input validation and basic statistical analysis.

## Features
- Log sensor readings with automatic timestamp
- View last N readings per tag
- Calculate statistics (average, min, max) per sensor
- Input validation against sensor specifications
- Automatic CSV file creation on first run

## Installation
*Coming soon*

## Usage
*Coming soon*

## Project Structure
```
process-logger/
├── process_logger.py      # Main program loop and menu
├── data_handler.py        # CSV read/write and data conversion
├── statistics.py          # Statistical calculations (avg, min, max)
├── test_statistics.py     # Unit tests
├── process_data.csv       # Data file (auto-generated)
└── README.md
```

## Sensor Specifications

| Sensor | Description  | Min  | Max | Unit   |
|--------|-------------|------|-----|--------|
| PI     | Pressure    | -1   | 25  | barg   |
| TI     | Temperature | 0    | 380 | °C     |
| FI     | Flow        | 0    | 200 | m3/hr  |

Readings outside these ranges will be rejected with a warning message.