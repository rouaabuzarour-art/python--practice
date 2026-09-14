# Python Capstone — End-to-End Triage Script

## Project Description

This project is a Python-based system triage tool designed to collect and analyze basic system information.

The application helps identify useful information about the computer, including running processes, file information, and file integrity using hashing.

## Features

- Collects basic system information.
- Lists running processes.
- Calculates file hashes to verify file integrity.
- Handles invalid input and errors safely.
- Uses modular Python code.
- Reads data from a CSV file.
- Includes unit tests using pytest.

## Project Structure

```text
capstone_project/
├── data/
│   └── sample_data.csv
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── utils.py
│   └── logic.py
├── tests/
│   └── test_logic.py
├── .gitignore
├── requirements.txt
└── README.md

Python 3.x

Install the required packages with:

pip install -r requirements.txt
How to Run

Run the main application with:

python src/main.py
Running Tests

To run the unit tests:

pytest

Technologies Used
Python
psutil
pytest
hashlib
subprocess
os

Error Handling

The application uses exception handling and input validation to prevent crashes caused by invalid input, missing files, or unexpected errors.

Purpose

The purpose of this project is to demonstrate practical Python programming skills, including modular programming, system interaction, error handling, file processing, hashing, data handling, and testing.