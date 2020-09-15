FROM python:3.8
WORKDIR /opt/accelbot
COPY . /opt/accelbot/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "bin/bot.py" ]