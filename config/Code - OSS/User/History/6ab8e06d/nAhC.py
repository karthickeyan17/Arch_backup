from flask import session, Flask, render_template ,request
from werkzeug.utils import secure_filename
import pandas as pd
import os 

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='uploads'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stats',methods=['POST'])
def find_stats():
    f = request.files.get('file')
    f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f)))

    session['file']=os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f))
    df = pd.read_csv('/home/karthi/Student_db.csv')
    return render_template('stats.html',tables=[df.to_html(classes='data')], titles=df.columns.values)
if __name__ == '__main__':
    app.run(debug=True)
