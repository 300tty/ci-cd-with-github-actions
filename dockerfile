# Builder stage
FROM python:3.9-slim as builder

WORKDIR /app

# Copy the requirements first to leverage Docker cache
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . ./


RUN ls -la tests/

# 运行测试
RUN pytest tests/
# Final image stage
FROM python:3.9-slim

# Create a non-root user
RUN useradd -m myuser
USER myuser

WORKDIR /app

# Copy application from builder stage
COPY --from=builder /app ./

# Expose port 5000 for the application
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Start the application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
