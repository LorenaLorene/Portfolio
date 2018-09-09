FROM python:3.6-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /usr/src/app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install Django

# Copy project
COPY . /usr/src/app

CMD cd /usr/src/app && python manage.py migrate && python manage.py runserver 0.0.0.0:8000