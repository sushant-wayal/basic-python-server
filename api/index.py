from flask import Flask

app = Flask(__name__)

@app.route('/api')
def catch_all(path):
    return 'Hello from Flask on Vercel!'