from flask import Flask

app = Flask(__name__)

@app.route('/')
def is_active():
    return 'line-bot起動中' 
