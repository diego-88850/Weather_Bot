FROM python:3.11-slim

WORKDIR /app

# Clean up any existing Google packages more thoroughly
RUN pip uninstall -y google google-auth google-auth-oauthlib google-auth-httplib2 google-api-core google-api-python-client google-cloud-core google-generativeai || true

# Clear pip cache
RUN pip cache purge

# Copy requirements first (for better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy files explicitly one by one to debug
COPY *.py .

# Debug: Show what we actually copied
RUN echo "=== Files in /app ===" && ls -la /app/
RUN echo "=== genai_weatherman.py content ===" && head -10 /app/genai_weatherman.py

# Ensure data directory exists
RUN mkdir -p /app/data

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]