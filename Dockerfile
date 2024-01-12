# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Poetry
RUN pip install poetry

# Install dependencies
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-dev

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Activate virtual environment and run the command
CMD ["bash", "-c", "source /app/.venv/bin/activate && poetry run python3 bot/main.py"]
