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
<<<<<<< HEAD
=======

CMD cd /usr/src/app && python manage.py runserver
>>>>>>> b0efcddb41a9b4e982ac76b6566601ac1f341d42
