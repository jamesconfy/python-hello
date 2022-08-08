from flask import Flask, jsonify
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info(f'Home Route')
    return "Hello World!"

@app.route("/status")
def status():
    response =  jsonify({
        "result": "OK - healthy",
        "code": 200
    })

    app.logger.info(f'Status Request Successful')
    return response, 200

@app.route("/metrics")
def metrics():
    response =  jsonify({
        "data": {"UserCount": 140, "UserCountActive": 23},
        "code": 200
    })

    app.logger.info(f'Metrics Request Successful')
    return response, 200

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
