FROM python:3.9-slim
LABEL MAINTAINER="Vasu Sharma <vasu.sharma@colorado.edu>"


WORKDIR /srv
COPY  requirements.txt /srv/requirements.txt
RUN pip3 install -r requirements.txt
COPY crons /srv/crons
COPY models /srv/models
COPY utils /srv/utils
COPY config.py /srv/config.py
COPY main.py /srv/main.py

CMD ["python3", "main.py"]