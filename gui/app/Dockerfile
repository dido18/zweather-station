FROM python:3

RUN  mkdir -p /home/app

ADD .  /home/app

RUN pip install -r /home/app/requirements.txt

WORKDIR /home/app

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD [ "flask", "run", "--host=0.0.0.0" ]
