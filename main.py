from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(message="Welcome to the CSY3056 Flask App!")

@app.route('/greet/<name>', methods=['GET'])
def greet(name):
    return jsonify(message=f"Hello, {name}!")

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    total = data.get('a', 0) + data.get('b', 0)
    return jsonify(result=total)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)