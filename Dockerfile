FROM ubuntu:latest

RUN useradd --user-group --create-home app

USER root

RUN apt-get update -y

RUN apt-get install -y  python3-pip python3-dev build-essential

COPY . /home/app

USER app

WORKDIR /home/app

USER root
RUN pip3 install -r requirements.txt

RUN chown -R app:app /home/app/*

CMD ["python","app.py"]