from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world... Hope you are doing well....This is to test our CI/CD pipeline'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
