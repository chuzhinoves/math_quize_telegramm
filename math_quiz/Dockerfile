FROM python:3.8.5
COPY requirements.txt /code/requirements.txt
WORKDIR /code
RUN pip install -r requirements.txt
COPY . /code
CMD gunicorn math_quiz.wsgi:application --bind 0.0.0.0:8000