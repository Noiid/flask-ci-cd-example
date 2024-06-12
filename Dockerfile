# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.11-slim

# Set the working directory to /app
RUN mkdir -p /app

# Copy file needed and setup work directory
COPY ./src /app
WORKDIR /app

# Install Pipenv
RUN pip install -U pipenv

# Install dependencies using Pipenv
RUN pipenv install --deploy

# Expose port 8080 for Gunicorn
EXPOSE 8080

# Run Gunicorn
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8080", "app:app"]
