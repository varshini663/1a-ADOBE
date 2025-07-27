# Use a lightweight Python image with AMD64 architecture
FROM --platform=linux/amd64 python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ /app/src/

# Create input and output directories
RUN mkdir -p /app/input /app/output

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the entrypoint
ENTRYPOINT ["python", "/app/src/main.py"]