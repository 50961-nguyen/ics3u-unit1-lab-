"""Prints the tier-capped grade after the test run (20 tests x 0.5 = 10 marks)."""

_passed = 0


def pytest_runtest_logreport(report):
    global _passed
    if report.when == "call" and report.passed:
        _passed += 1


def pytest_terminal_summary(terminalreporter):
    grade = _passed * 0.5
    terminalreporter.write_sep("=", "GRADE")
    terminalreporter.write_line(f"GRADE: {grade:g}/10 ({_passed}/20 tests passed)")
