from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, world!"


def call_round_api():
    return "Calling round api"

