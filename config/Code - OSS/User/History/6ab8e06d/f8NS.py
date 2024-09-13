from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

DB_PATH = 'path/to/db.csv'
OUTPUT_PATH = 'path/to/output.csv'

def process_stats(val, name, rollno):
    if not val:
        val = {'Easy': 0, 'Medium': 0, 'Hard': 0}
    return pd.DataFrame(val, index=[f"{rollno}-{name}"])

def fetch_stats(date):
    df = pd.read_csv(DB_PATH)
    stats = []

    for index, row in df.iterrows():
        problems_by_date = Scraper.getProblems(row['Leetcode ID'])
        val = problems_by_date.get(date)
        stats.append(process_stats(val, row['Name'], row['Roll No.']))
        if len(stats) == 3:
            break

    df2 = pd.concat({date: pd.concat(stats, axis=0)}, axis=1, names=['Date', 'Difficulty'])

    if os.path.isfile(OUTPUT_PATH):
        df1 = pd.read_csv(OUTPUT_PATH, header=[0, 1], index_col=[0])
        if date in df1.columns.get_level_values(0):
            df1 = df1.drop(columns=date, level=0)
        df2 = df1.merge(df2, left_index=True, right_index=True, how='outer')

    df2.to_csv(OUTPUT_PATH)
    return df2

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
