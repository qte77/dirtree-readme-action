# https://github.com/athul/waka-readme/blob/master/dockerfile
FROM docker.io/python:3-slim
ENV WD="./app" \
    ENTRY="./app/app.py" \
    USER="app" \
    # python
    # PATH="${PATH}:/root/.local/bin" \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=100
RUN groupadd $USER && \
    useradd --no-log-init -g $USER $USER
COPY --chown=$USER:$USER --chmod=0755 $WD $WD
USER $USER
RUN whoami
RUN echo $ENTRY
RUN env
# RUN python -m pip install .
# CMD ["python", ${wd}/app.py]
ENTRYPOINT ["python", $ENTRY]
