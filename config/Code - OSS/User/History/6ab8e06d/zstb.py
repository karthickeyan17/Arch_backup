from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stats', methods=['POST'])
def stats():
    date = request.form['date']
    df2 = fetch_stats(date)
    return render_template('stats.html', tables=[df2.to_html(classes='data')], titles=df2.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
