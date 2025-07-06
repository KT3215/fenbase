FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose port
EXPOSE 8000

# Run Django dev server (update if using Gunicorn in prod)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
