from flask import Flask

app = Flask(__name__)

@app.route('/api')
def home():
    return 'Hello from Flask on Vercel!'

@app.route('/api/<path:path>')
def catch_all(path):
    return f'You hit: /api/{path}'
