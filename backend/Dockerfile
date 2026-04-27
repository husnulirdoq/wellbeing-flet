FROM python:3.11-slim

WORKDIR /app

# Copy requirements dulu biar cache efisien
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy semua source code
COPY . .

# Jalankan FastAPI pakai uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
