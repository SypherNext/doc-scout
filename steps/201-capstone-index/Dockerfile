# syntax=docker/dockerfile:1
# Multi-stage build: dependencies and the package are installed in
# "builder" into a user site-packages directory, and only that directory
# plus the application code are copied into the slim runtime stage -- no
# compilers or build caches ship in the final image. Follows the Docker
# lesson's production-ready pattern.

FROM python:3.12-slim AS builder

WORKDIR /app

COPY pyproject.toml ./
COPY configs ./configs
COPY src ./src

RUN pip install --no-cache-dir --user .

FROM python:3.12-slim AS runtime

WORKDIR /app

# Non-root user: running as root inside the container is an unnecessary
# privilege-escalation risk (Docker lesson, Security Considerations).
RUN groupadd -r appuser && useradd -r -g appuser -d /app appuser

COPY --from=builder /root/.local /home/appuser/.local
COPY --from=builder /app/configs ./configs

ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1

RUN mkdir -p /app/rag_db /app/cache /app/logs \
    && chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "research_assistant.main:app", "--host", "0.0.0.0", "--port", "8000"]
