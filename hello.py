from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app= Flask(__name__)
#add database
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///users.db'
#secretkey

app.config['SECRET_KEY']= "any password"
db = SQLAlchemy(app)
#create model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
#create a string
    def __repr__(self):
       return f"<Name {self.name}>"
      
class UserForm(FlaskForm):
    name =StringField("Name", validators=[DataRequired()])
    email =StringField("Email", validators=[DataRequired()])                  
    submit = SubmitField("submit")     


#create a form class

class NamerForm(FlaskForm):
    name =StringField("what is your name", validators=[DataRequired()])
    submit = SubmitField("submit")
                                        



@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    form=UserForm()
    return render_template("add_user.html", form=form) 
          
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', name=name)

#invalid url

@app.errorhandler(404)
def page_not_found(e):    
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name= None
    form= NamerForm()

    if form.validate_on_submit():
        name =form.name.data
        form.name.data =''
        flash("Great Your Form Submitted Successfully!")
    return render_template("name.html", 
         name =name,
        form= form )                   
                           

 
