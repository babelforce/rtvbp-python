# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY requirements.txt server.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose WebSocket port
EXPOSE 8765

# Run the server
CMD ["python", "server.py"]
