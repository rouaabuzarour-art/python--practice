import sys

from logic import run_triage
from utils import validate_folder, save_report


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "data/sample_evidence"

    try:
        validate_folder(folder)

        report = run_triage(folder)
        save_report(report, "data/triage_report.json")

        print("\nReport saved to data/triage_report.json")

    except ValueError as error:
        print(f"Error: {error}")

    except OSError as error:
        print(f"Error accessing folder: {error}")