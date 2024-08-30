# Dockerfile

# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Django project files into the container
COPY . .

# Set the environment variable for Django
ENV PYTHONUNBUFFERED 1

# Expose the port on which Django runs
EXPOSE 8000

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
