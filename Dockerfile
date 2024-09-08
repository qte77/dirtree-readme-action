# https://github.com/athul/waka-readme/blob/master/dockerfile
FROM docker.io/python:3-slim
ENV WD="/app" \
    ENTRY="${WD}/app.py" \
    # python
    # PATH="${PATH}:/root/.local/bin" \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1
    # pip
    # PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # PIP_NO_CACHE_DIR=1 \
    # PIP_DEFAULT_TIMEOUT=100
ARG user="app"
RUN groupadd $user && \
    useradd --no-log-init -g $user $user
COPY --chown=$user:$user --chmod=0755 $WD $WD
USER $user
RUN echo $ENTRY
RUN env
# RUN python -m pip install .
# CMD ["python", ${wd}/app.py]
ENTRYPOINT ["python", $ENTRY]
