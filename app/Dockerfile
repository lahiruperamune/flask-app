# Use the official Python base image
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY service.py .

# Expose the port that the Flask app will be running on
EXPOSE 5000

# Set the command to run the Python script
CMD ["python", "service.py"]
