from flask import Flask

app = Flask(__name__)

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'