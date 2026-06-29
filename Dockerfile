FROM python:3.11-slim
WORKDIR /proyecto-entregable-4
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]