FROM python:3.11.4

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED=1

RUN mkdir /sd-webui

WORKDIR sd-webui

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x deploy/*.sh
