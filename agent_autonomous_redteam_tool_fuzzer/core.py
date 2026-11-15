"""Core tool fuzzer implementation."""
from typing import Callable, Any, List

class FuzzReport:
    def __init__(self, total_tests: int, failures: int, crash_samples: List[Any]):
        self.total_tests = total_tests
        self.failures = failures
        self.crash_samples = crash_samples

class ToolFuzzer:
    PATHOLOGICAL_SEEDS = [
        "",
        "\x00",
        "../../../etc/passwd",
        "A" * 5000,
        "%s%s%s%s",
        "\n\r\t",
        "null",
        "-1",
    ]

    @classmethod
    def fuzz(cls, target_function: Callable[[str], Any]) -> FuzzReport:
        crashes = []
        for seed in cls.PATHOLOGICAL_SEEDS:
            try:
                target_function(seed)
            except Exception as e:
                crashes.append({"seed": seed[:20], "error": str(e)})

        return FuzzReport(len(cls.PATHOLOGICAL_SEEDS), len(crashes), crashes)
