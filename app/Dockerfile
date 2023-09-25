FROM python:3.11-slim
COPY . /backend/
WORKDIR /backend
ENV PYTHONDONTWRITEBYTECODE 1
RUN pip install -r \
    requirements.txt