#
# Dockerfile for the WanikaniReverse backend
#

#Start from a Python 3 docker image
FROM python:3

#Copy Pipfiles to /opt/mattrosanio/wanikanireverse
RUN mkdir -p /opt/mattrosanio/wanikanireverse
COPY Pipfile /opt/mattrosanio/wanikanireverse
COPY Pipfile.lock /opt/mattrosanio/wanikanireverse
COPY init.sh /opt/mattrosanio/wanikanireverse
COPY . /opt/mattrosanio/wanikanireverse/backend
WORKDIR /opt/mattrosanio/wanikanireverse
RUN chmod +x init.sh

#Install and update python packages and project dependencies
RUN pip install pipenv==2018.11.26 && \
    pipenv install --system --deploy

#Update apt
RUN apt -y update

#Install gunicorn web server
RUN apt-get -y --no-install-recommends install gunicorn=19.6.0-10+deb9u1
EXPOSE 8001


