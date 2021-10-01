import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api')
def index():
    with open('static/banlist.json', 'r') as fp:
        payload = json.load(fp)
    return jsonify(payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)