"""Cross-cutting behaviour for LLM calls: retry and logging.

retry_with_backoff retries a wrapped call that raises LLMAPIError,
with exponential backoff between attempts.

log_calls logs entry, exit, and timing for the wrapped call.
"""
import functools
import logging
import time

from .exceptions import LLMAPIError

logger = logging.getLogger(__name__)


def retry_with_backoff(func):
    """Retry func on LLMAPIError, doubling the delay after each attempt."""

    @functools.wraps(func)
    def wrapper(*args, max_attempts: int = 3, base_delay: float = 0.5, **kwargs):
        attempt = 1
        while True:
            try:
                return func(*args, **kwargs)
            except LLMAPIError as exc:
                if attempt >= max_attempts:
                    logger.error("%s failed after %d attempts: %s", func.__name__, attempt, exc)
                    raise
                delay = base_delay * (2 ** (attempt - 1))
                logger.warning(
                    "%s raised %s on attempt %d/%d, retrying in %.2fs",
                    func.__name__, exc, attempt, max_attempts, delay,
                )
                time.sleep(delay)
                attempt += 1

    return wrapper


def log_calls(func):
    """Log entry, exit, and timing for every call to func."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("-> %s(args=%r, kwargs=%r)", func.__name__, args, kwargs)
        start = time.perf_counter()
        try:
            result = func(*args, **kwargs)
        except Exception:
            logger.exception("x  %s raised", func.__name__)
            raise
        elapsed = time.perf_counter() - start
        logger.info("<- %s returned in %.3fs", func.__name__, elapsed)
        return result

    return wrapper
