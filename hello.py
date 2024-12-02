from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')

def index():
    return "<h1>Hello world</h1>"

@app.route('/user/<name>')

def user(name):
    return f"<h1>Hello {name}</h1>"

#invalid url

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
 
