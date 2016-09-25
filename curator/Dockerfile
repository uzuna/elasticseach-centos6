FROM python:3.6

VOLUME "/apps"

RUN apt update
RUN apt-get install cron -y && apt-get clean
RUN pip install elasticsearch-curator
RUN pip install schedule

WORKDIR /apps
