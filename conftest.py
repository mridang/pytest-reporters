# Root conftest.py - registers BetterCoverage reporter
from spec import better_coverage


def pytest_addoption(parser):
    """Register command-line options for BetterCoverage."""
    better_coverage.pytest_addoption(parser)


def pytest_configure(config):
    """Configure BetterCoverage reporter."""
    better_coverage.pytest_configure(config)


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """Generate BetterCoverage report at end of test run."""
    better_coverage.pytest_terminal_summary(terminalreporter, exitstatus, config)
