import sys
import os
import pathlib

RECENTS_FILE_NAME = "recents.txt"

def home_path():
    return pathlib.Path.home()

def recents_path():
    return home_path() / RECENTS_FILE_NAME

def print_usage():
    print("usage: " + sys.argv[0] + " LINE_NUMBER")

def get_recent(line_number: int) -> str:
    lines = None
    with open(recents_path(), mode='r') as recents_file:
        lines = recents_file.readlines()

    if lines is None:
        raise Error("Failed to read lines from file")

    if len(lines) < line_number:
        return ""

    return lines[line_number - 1].strip()

def print_recents():
    lines = None
    with open(recents_path(), mode='r') as recents_file:
        lines = recents_file.readlines()

    if lines is None:
        raise Error("Failed to read lines from file")

    i = 1
    for line in lines:
        print(str(i) + ") " + line.strip())
        i += 1

def main():
    # process arguments
    if len(sys.argv) > 2:
        print_usage()
        sys.exit(1)

    if len(sys.argv) == 1:
        print_recents()
        sys.exit(0)

    line_number = int(sys.argv[1])
    print(get_recent(line_number))

main()

