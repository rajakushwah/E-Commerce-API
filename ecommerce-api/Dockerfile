# Dockerfile

FROM python:3.11

WORKDIR /app
COPY . /app
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
