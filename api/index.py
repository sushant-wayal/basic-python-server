from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask on Vercel!'

@app.route('/<path:path>')
def catch_all(path):
    return f'You hit: /{path}'