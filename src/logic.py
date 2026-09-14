import os
import time
import hashlib


def check_processes():
    """Return a short list of running process names and PIDs."""

    try:
        import psutil

        return [
            process.info
            for process in psutil.process_iter(["pid", "name"])
        ][:5]

    except ImportError:
        return []


def check_recent_files(folder, window_seconds=600):
    """Return files modified within the given time window."""

    current_time = time.time()
    recent = []

    for name in os.listdir(folder):
        path = os.path.join(folder, name)

        if os.path.isfile(path):
            mtime = os.stat(path).st_mtime

            if current_time - mtime <= window_seconds:
                age = int(current_time - mtime)
                recent.append((name, age))

    return recent


def check_hashes(folder):
    """Return a dictionary containing SHA-256 hashes for files."""

    hashes = {}

    for name in os.listdir(folder):
        path = os.path.join(folder, name)

        if os.path.isfile(path):
            with open(path, "rb") as file:
                digest = hashlib.sha256(file.read()).hexdigest()
                hashes[name] = digest

    return hashes

def run_triage(folder="data/sample_evidence"):
    """Run all triage checks and return the results."""

    processes = check_processes()
    recent = check_recent_files(folder)
    hashes = check_hashes(folder)

    print(f"--- Triage Report for '{folder}' ---")

    print("\nRunning Processes:")
    for process in processes:
        print(" ", process)

    print("\nRecently Modified Files:")
    if recent:
        for name, age in recent:
            print(f"  {name} ({age}s ago)")
    else:
        print("  none")

    print("\nFile Hashes:")
    for name, digest in hashes.items():
        print(f"  {name}: {digest[:12]}...")

    return {
        "folder": folder,
        "processes": processes,
        "recent_files": recent,
        "hashes": hashes,
    }