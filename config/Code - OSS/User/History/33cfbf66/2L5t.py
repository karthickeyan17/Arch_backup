from flask import Flask
app =Flask()
@app.route('/')
def home():
    return  "hai maple"