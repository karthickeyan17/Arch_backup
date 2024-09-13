from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
import pandas as pd
import os

ALLOWED_EXTENSIONS = {'csv'}  # Set of allowed file extensions

app = Flask(__name__)
app.config['FILE_UPLOADS'] = '/home/karthi/leetcode-stats-frontend/static/'  # Replace with your upload directory

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

            if not allowed_file(filename):
                return render_template('stats.html', error="Invalid file format. Please upload a CSV file.")

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
