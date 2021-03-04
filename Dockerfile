FROM python:3.9-slim

ENV PYTHONWARNINGS=ignore
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG SUSERNAME=azvaultdemo
ARG APP_DIR=/tmp/${SUSERNAME}

RUN adduser --system ${SUSERNAME}

RUN apt update && apt upgrade -y

RUN mkdir -p ${APP_DIR}

WORKDIR ${APP_DIR}

ADD ./setup.py ./setup.py
ADD ./vault_app ./vault_app

RUN python setup.py install

USER ${SUSERNAME}

ENTRYPOINT ["vaultapp"]