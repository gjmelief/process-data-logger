## Installation

### Requirements
- Python 3.x
- No external dependencies required (uses standard library only)

### Setup
1. Clone the repository:
```bash
git clone https://github.com/gjmelief/process-data-logger.git
cd process-data-logger
```

2. Run the program:
```bash
python process_logger.py
```

The program will automatically create `process_data.csv` on first run.

## Usage

Run the main program:
```bash
python process_logger.py
```

### Menu Options

**1. Log Data**
- Enter sensor tag (e.g., PI-001, TI-002, FI-003)
- Enter process value
- Values are validated against sensor specifications
- Invalid values are rejected with an error message

**2. View Data**
- Select a sensor tag
- Specify number of readings to display
- Shows the most recent N readings with timestamps

**3. View Statistics**
- Select a sensor tag
- Choose statistic: Average, Minimum, or Maximum
- Displays calculated result

**4. Exit**
- Closes the program

### Example Session
```
---Menu---
1. Log Data
2. View Data
3. View Statistics
4. Exit the program
Choose option from above: 1

---Log Data menu---
What tag do you want to log a value for? PI-001
What is the process value? 2.3
Reading logged successfully.

Do you want to log another reading? y/n: n
```