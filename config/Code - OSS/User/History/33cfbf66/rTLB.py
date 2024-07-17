from flask import flask
app =flask()
@app.route('/')
def home():
    return  "hai maple"