# use a python base image for container
FROM python:3.11

#copies requirements.txt into image
COPY ./requirements.txt .

#installs dependencies
RUN pip install -r requirements.txt

# copies entrypoint.py into container image
COPY ./entrypoint.py .

CMD exec gunicorn entrypoint:app
