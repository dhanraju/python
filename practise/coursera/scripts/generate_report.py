#!/usr/bin/env python3

import csv

def read_employees(csv_file_location):
    """takes file_location (path to employees.csv) as a parameter."""
    # Open the CSV file by calling open and then csv.DictReader.
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')