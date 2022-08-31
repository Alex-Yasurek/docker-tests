FROM python:3.8

RUN pip install flask

WORKDIR /opt/app

COPY . .

ENV FLASK_APP=app.py

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
