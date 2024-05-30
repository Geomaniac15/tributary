# Use a python base image for container
FROM python:3.11

# Copies requirements.txt into image
COPY ./requirements.txt .

# Installs dependencies
RUN pip install -r requirements.txt

# Copies entrypoint.py into container image
COPY ./entrypoint.py .

# Sets the command to run the Gunicorn server
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "entrypoint:app"]
# -w 4: specifies number of worker processes, concurrent instances of a program
# -b 0.0.0.0:8000: binds all netowkr ionterfaces on port 8000
