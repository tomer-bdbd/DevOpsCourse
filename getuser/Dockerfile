FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt ./

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py ./

# Expose the port
EXPOSE 5000

# Run the application directly with python
CMD ["python", "main.py"]