#!/usr/bin/env python3
"""Entry point: start the Uvicorn dev server for the research assistant API."""

from __future__ import annotations

import uvicorn

from research_assistant.config import load_config


def main() -> None:
    settings = load_config()
    uvicorn.run(
        "research_assistant.main:app",
        host="0.0.0.0",
        port=settings.port,
        reload=True,
    )


if __name__ == "__main__":
    main()
