from flask import Request, session, Flask, render_template ,request
from werkzeug.utils import secure_filename
import pandas as pd
import os 

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='/home/karthi/leetcode-stats-frontend/uploads'
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/stats',methods=['GET','POST'])
def find_stats():
    data=[]
    df = pd.DataFrame()
    if request.method=="POST" and request.files:
        uf = request.files['file']
        path = os.path.join(app.config['UPLOAD_FOLDER',uf.filename])
        uf.save(path)
        # session['file']=os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f))
        df = pd.read_csv(path)
    return render_template('stats.html',tables=[df.to_html(classes='data')], titles=df.columns.values)
if __name__ == '__main__':
    app.run(debug=True)
