"""CLI for Tool Fuzzer."""
import argparse
from .core import ToolFuzzer

def safe_reader(path: str):
    if "\x00" in path or ".." in path:
        return "Rejected invalid path"
    return f"Read {len(path)} chars"

def main():
    parser = argparse.ArgumentParser(description="Tool Fuzzer CLI")
    parser.add_argument("--demo", action="store_true", help="Demonstrate tool fuzzing")
    args = parser.parse_args()

    report = ToolFuzzer.fuzz(safe_reader)
    print(f"Fuzz tests run: {report.total_tests}")
    print(f"Crashes/Exceptions detected: {report.failures}")

if __name__ == "__main__":
    main()
