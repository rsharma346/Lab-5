#!/usr/bin/env python3

# lab5b.py

# Function to append a string to a file
def append_file_string(file_name, string_of_lines):
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

# Function to write a list of lines to a file
def write_file_list(file_name, list_of_lines):
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

# Function to copy content from one file to another, adding line numbers
def copy_file_add_line_numbers(file_name_read, file_name_write):
    with open(file_name_read, 'r') as read_file:
        lines = read_file.readlines()

    with open(file_name_write, 'w') as write_file:
        for i, line in enumerate(lines, 1):
            write_file.write(f"{i}:{line}")

# Function to read a file content as a string
def read_file_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()

# Function to read a file content as a list of lines without newlines
def read_file_list(file_name):
    with open(file_name, 'r') as f:
        # Strip the newline character from each line
        return [line.strip() for line in f.readlines()]

# Main program
if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    
    append_file_string(file1, string1)
    print(read_file_string(file1))
    
    write_file_list(file2, list1)
    print(read_file_string(file2))
    
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))

