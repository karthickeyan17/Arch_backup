from flask import Flask, render_template, request, redirect, secure_filename
from werkzeug.utils import secure_filename
import pandas as pd
import os

app = Flask(__name__)
app.config['FILE_UPLOADS'] = '/home/karthi/leetcode-stats-frontend/uploads'  # Replace with your upload directory

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/stats', methods=['GET', 'POST'])
def stats():
    data = []
    if request.method == 'POST':
        if request.files:
            print('Received file')
            uploaded_file = request.files['file']
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(app.config['FILE_UPLOADS'], filename)
            uploaded_file.save(filepath)

            try:
                df = pd.read_csv(filepath)
                tables = [df.to_html(classes='data')]  # Convert DataFrame to HTML table
                titles = [df.columns.values]  # Extract column names as title
            except Exception as e:  # Handle potential errors during file reading
                print(f"Error processing file: {e}")
                return render_template('stats.html', error="Error processing file")

            return render_template('stats.html', tables=tables, titles=titles)
    return render_template('stats.html')


if __name__ == '__main__':
    app.run(debug=True)

