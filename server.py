import json

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/receiver/movie', methods=['POST'])
def receive():
    content = json.loads(request.data)
    print(content)
    # to something
    return jsonify({'status': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
