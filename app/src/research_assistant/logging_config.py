"""Console + rotating-file logging, following the Logging lesson's
``PipelineLogger`` pattern: a concise INFO console stream for request
summaries, and a detailed DEBUG file trail for every pipeline stage.
"""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

CONSOLE_FORMAT = "[%(levelname)s] %(message)s"
FILE_FORMAT = "%(asctime)s [%(levelname)s] %(name)s:%(lineno)d: %(message)s"

LOGGER_NAME = "research_assistant"


def configure_logging(
    log_dir: str | Path = "./logs",
    filename: str = "research_assistant.log",
    console_level: int = logging.INFO,
    file_level: int = logging.DEBUG,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 3,
) -> logging.Logger:
    """Configure the shared ``research_assistant`` logger.

    Idempotent: existing handlers are cleared first, so calling this more
    than once (once in ``main.py``, once in a test fixture) never produces
    duplicate log lines.

    Args:
        log_dir: Directory the rotating file handler writes into. Created
            if it does not exist.
        filename: Name of the log file inside ``log_dir``.
        console_level: Minimum level printed to stderr.
        file_level: Minimum level written to the log file.
        max_bytes: Rotate the file once it exceeds this size.
        backup_count: Number of rotated files to keep.

    Returns:
        The configured logger. Every module in the package should call
        ``logging.getLogger(__name__)`` and rely on this configuration
        rather than re-configuring handlers itself.
    """
    logger = logging.getLogger(LOGGER_NAME)
    logger.handlers.clear()
    logger.setLevel(min(console_level, file_level))
    logger.propagate = False

    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    console_handler.setFormatter(logging.Formatter(CONSOLE_FORMAT))
    logger.addHandler(console_handler)

    log_path = Path(log_dir)
    log_path.mkdir(parents=True, exist_ok=True)
    file_handler = RotatingFileHandler(
        log_path / filename,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )
    file_handler.setLevel(file_level)
    file_handler.setFormatter(logging.Formatter(FILE_FORMAT))
    logger.addHandler(file_handler)

    return logger
