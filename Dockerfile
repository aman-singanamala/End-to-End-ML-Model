# DockerFile . Image, Container
FROM python:3.11.2

ADD app.py .


# Install additional dependencies
RUN pip install flask joblib numpy


CMD ["python", "./app.py"]




