FROM python:3.7.0-alpine3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Make app.py available
COPY app.py .

EXPOSE 80

CMD ["python", "app.py"]
