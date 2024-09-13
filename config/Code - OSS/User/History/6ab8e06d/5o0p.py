from flask import render_template, Flask

app = Flask(__name__)
app.route('/')
def home():
    render_template()