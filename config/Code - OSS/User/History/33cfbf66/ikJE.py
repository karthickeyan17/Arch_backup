from flask import Flask

app = Flask(__name__)
@app.route('/<n>')
def home(n):
    return f'{n}'
if(__name__=='__main__'):
    app.run()