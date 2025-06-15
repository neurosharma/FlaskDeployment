from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!ergregre</p>"

@app.route('/pagetwo')
def page():
    return render_template('page2.html')