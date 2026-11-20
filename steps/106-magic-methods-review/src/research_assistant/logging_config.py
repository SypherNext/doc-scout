"""Central logging setup for the research assistant.

Call configure_logging() once, at the entry point of a script or
service, before any other research_assistant code logs anything.
"""
import logging
import sys


def configure_logging(level: int = logging.INFO, log_file: str | None = None) -> None:
    """Configure the root logger with a console handler, and optionally
    a file handler as well."""
    handlers: list[logging.Handler] = [logging.StreamHandler(sys.stdout)]
    if log_file:
        handlers.append(logging.FileHandler(log_file, encoding="utf-8"))

    for handler in handlers:
        handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        ))

    root = logging.getLogger()
    root.setLevel(level)
    root.handlers = handlers
