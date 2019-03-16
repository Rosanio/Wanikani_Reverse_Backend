#
# Dockerfile for the WanikaniReverse backend
#

#Start from a Python 3 docker image
FROM python:3

#Copy Pipfiles to /opt/mattrosanio/wanikanireverse
RUN mkdir -p /opt/mattrosanio/backend
COPY Pipfile /opt/mattrosanio/backend
COPY Pipfile.lock /opt/mattrosanio/backend
WORKDIR /opt/mattrosanio/backend

#Install and update python packages and project dependencies
RUN pip install pipenv && \
    pipenv install --system --deploy

#Update apt
RUN apt -y update

#Install gunicorn web server
RUN apt-get -y --no-install-recommends install gunicorn=19.6.0-10+deb9u1
EXPOSE 8001


