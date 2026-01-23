# 1. Official lightweight Python image
FROM python:3.10-slim

# 2. Critical for Cloud Run: Ensure logs are sent directly to the console 
# without being buffered, so you can debug in real-time.
ENV PYTHONUNBUFFERED True

# 3. Establish the working directory
WORKDIR /app

# 4. Optimization: Copy requirements first to leverage Docker's cache.
# This makes subsequent builds much faster if your code changes but libraries don't.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the application code
COPY . .

# 6. Production-grade execution
# Cloud Run injects $PORT (8080). --timeout 0 is recommended by Google.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app