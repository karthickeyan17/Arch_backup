from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stats'):
    return 
if __name__ == '__main__':
    app.run(debug=True)
