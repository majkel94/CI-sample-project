from flask import Flask

import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return json.dumps("{'foo': 'fail'}")
