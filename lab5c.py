#!/usr/bin/env python3
# Author ID: rsharma346

def add(number1, number2):
    try:
        # Try to convert both inputs to integers (or floats) before adding
        number1 = int(number1) if isinstance(number1, str) else number1
        number2 = int(number2) if isinstance(number2, str) else number2
        return number1 + number2
    except (ValueError, TypeError):
        # Return an error message if conversion fails or there's a type mismatch
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return 'error: could not read file'

if __name__ == '__main__':
    # Test cases
    print(add(10, 5))                        # works: 15
    print(add('10', 5))                      # works: 15
    print(add('abc', 5))                     # exception: error: could not add numbers
    print(add('10', '5'))                    # works: 15
    print(read_file('seneca2.txt'))          # works: ['Line 1\n', 'Line 2\n', 'Line 3\n']
    print(read_file('file10000.txt'))        # exception: error: could not read file

