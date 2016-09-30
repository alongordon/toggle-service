FROM python:3.5.2
ENV PYTHONUNBUFFERED 1
ENV WITH_DOCKER True
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin python-dev python3-lxml
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/