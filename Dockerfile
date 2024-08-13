# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django application code into the container
COPY . /app/

EXPOSE 8000

# Run the Gunicorn server
CMD ["gunicorn", "backend.wsgi:application", "--config", "gunicorn_config.py"]
