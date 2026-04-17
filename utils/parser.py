import re

def extract_errors(logs):
    lines = logs.split("\n")
    error_lines = []

    for line in lines:
        if re.search(r'error|fail|exception', line, re.IGNORECASE):
            error_lines.append(line)

    return error_lines[:20]
