# https://github.com/athul/waka-readme/blob/master/dockerfile
FROM docker.io/python:3-slim
ENV PATH="${PATH}:/root/.local/bin" \
    # python
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1
    # pip
    # PIP_DISABLE_PIP_VERSION_CHECK=1 \
    # PIP_NO_CACHE_DIR=1 \
    # PIP_DEFAULT_TIMEOUT=100
ARG user=app
ARG wd=/app
RUN groupadd $user && \
    useradd --no-log-init -g $user -ms /bin/bash $user
WORKDIR $wd
COPY --chown=$user:$user $wd .
USER $user
# RUN python -m pip install .
# CMD python app.py
RUN echo $PWD
RUN dir
RUN dir $wd
RUN dir /
