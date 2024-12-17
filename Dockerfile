FROM python:3

WORKDIR /usr/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/wifimonk .

COPY ./tests ./tests

CMD [ "python", "./your-daemon-or-script.py" ]