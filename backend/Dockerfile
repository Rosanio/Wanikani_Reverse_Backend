#
# Dockerfile for the WanikaniReverse backend
#

#Start from a Python 3 docker image
FROM python:3.7-stretch

# Install Python dependencies
RUN mkdir -p /opt/mattrosanio/backend
COPY Pipfile Pipfile.lock /opt/mattrosanio/backend/
WORKDIR /opt/mattrosanio/backend
RUN pip install pipenv && \
    pipenv install --system --deploy

# Set flask app environmental variable so it is available in the bash shell
ENV FLASK_APP main.py
