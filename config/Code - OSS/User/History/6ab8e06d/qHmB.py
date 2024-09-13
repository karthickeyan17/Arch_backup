from flask import Flask, render_template

import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stats')
def find_stats():
    #data_frame
    df = pd.read_csv('/home/karthi/Student_db.csv')
    return render_template('stats.html',df.to_html(header="true", table_id="table"))
if __name__ == '__main__':
    app.run(debug=True)
