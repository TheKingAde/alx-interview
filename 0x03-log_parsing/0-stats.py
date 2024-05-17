#!/usr/bin/python3
import sys
import signal

# Initialize metrics
total_file_size = 0
status_code_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
valid_status_codes = set(status_code_counts.keys())

def print_statistics():
    """Print the collected statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handle the keyboard interruption to print the statistics."""
    print_statistics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        
        # Validate the line format
        if len(parts) >= 7 and parts[5] == '"GET' and parts[6] == '/projects/260' and parts[7] == 'HTTP/1.1"':
            ip_address = parts[0]
            date = parts[3][1:] + " " + parts[4][:-1]  # [date] -> date
            status_code = parts[8]
            file_size = parts[9]

            try:
                file_size = int(file_size)
                total_file_size += file_size
            except ValueError:
                continue

            if status_code in valid_status_codes:
                status_code_counts[status_code] += 1
            
            line_count += 1

            if line_count % 10 == 0:
                print_statistics()
except KeyboardInterrupt:
    print_statistics()
    sys.exit(0)
