FROM python:3.10-slim
LABEL owner "James Confidence"

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "app.py" ]