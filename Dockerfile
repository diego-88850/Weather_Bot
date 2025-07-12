FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Ensure logs directory exists
RUN mkdir -p /app/data

# Default command (run your app)
CMD ["python", "main.py"]