import os
import json


def validate_folder(folder):
    """Check whether the given path is a valid folder."""

    if not os.path.isdir(folder):
        raise ValueError(f"'{folder}' is not a valid folder.")

    return True




def save_report(report, output_file):
    """Save the triage report to a JSON file."""

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)