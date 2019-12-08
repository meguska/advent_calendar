from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from models import pernicky

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    #print(get_activities)
    return render_template('index.html')

@app.route('/sdetmi/')
def sdetmi():
   return render_template("sdetmi.html")

@app.route('/pernicky/<id>', methods=['GET'])
def pernicky(id):
    #pernicky = db.pernicky(id)
    return render_template("pernicky.html")

@app.route('/singles/')
def singles():
   return render_template("singles.html")

#error handelers
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.errorhandler(500)
def pagenot_found(e):
    return render_template("500.html")
