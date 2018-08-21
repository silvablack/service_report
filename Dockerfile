FROM ubuntu:latest

RUN useradd --user-group --create-home --shell /bin/false app

USER root

RUN apt-get update -y

RUN apt-get install -y  python-pip python-dev build-essential

COPY . /home/app

USER app

WORKDIR /home/app

USER root
RUN pip install -r requirements.txt

RUN chown -R app:app /home/app/*

CMD ["python","app.py"]