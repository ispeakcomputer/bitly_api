# Base Image 
FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 
# create and set working directory
RUN mkdir /app
WORKDIR /app
#Add code
ADD . /app/
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt && chmod +x start_here.sh

CMD ./start_here.sh
