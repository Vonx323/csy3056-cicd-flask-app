from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a CI/CD Test App."

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
