# Dockerfile
FROM python:3.12

WORKDIR /app

# Copy all necessary files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Command to initialize the database and run the Flask application
#CMD ["python", "app/init_db.py"]
CMD ["python", "app/app.py"]
