# https://github.com/athul/waka-readme/blob/master/dockerfile
FROM docker.io/python:3.12-slim

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=100

RUN useradd -U appuser
WORKDIR /app
COPY --chown=appuser:appuser ./app/app.py ./app/utils.py /app/
COPY --chown=appuser:appuser ./requirements.txt /app/
RUN set -xe && \
    python -m pip install -r requirements.txt
CMD ["python", "app.py"]
