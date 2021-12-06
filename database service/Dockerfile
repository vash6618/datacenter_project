FROM python:3.9-slim
LABEL MAINTAINER="Vasu Sharma <vasu.sharma@colorado.edu>"


WORKDIR /srv
COPY  requirements.txt /srv/requirements.txt
RUN pip3 install -r requirements.txt
COPY models /srv/models
COPY routes /srv/routes
COPY config.py /srv/config.py
COPY main.py /srv/main.py
COPY pod-key.json /srv/pod-key.json
CMD ["python3", "main.py"]