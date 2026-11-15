"""Automated test suite for Tool Fuzzer."""
import unittest
from agent_autonomous_redteam_tool_fuzzer.core import ToolFuzzer

class TestToolFuzzer(unittest.TestCase):
    def test_fuzzer_executes_suite(self):
        def robust_tool(val: str):
            return len(val)

        report = ToolFuzzer.fuzz(robust_tool)
        self.assertEqual(report.failures, 0)
