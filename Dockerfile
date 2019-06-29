FROM python:3.6.6
MAINTAINER Ian Roberts <admin@tangentsolutions.co.za>

ENV PYTHONUNBUFFERED 1
ENV WITH_DOCKER True
RUN apt-get update && apt-get install -y --no-install-recommends binutils libproj-dev gdal-bin python-dev python3-lxml \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
RUN mkdir /var/log/celery
RUN chmod 777 -R /var/log/celery
COPY etc/supervisor/conf.d/. /etc/supervisor/conf.d/
COPY . /code/
