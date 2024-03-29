from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random, array
import databaza
from databaza import pernicky1


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route('/')
def home():
    #print(get_activities)
    return render_template('index.html')

@app.route('/sdetmi/', methods=['GET'])
def sdetmi():
    pole= array.array('i', (i for i in range(1,25)))
    random.shuffle(pole)
    return render_template("sdetmi.html", pole=pole)

app.route('/pernicky/')
def pernicky2():
    return render_template("pernicky.html")

@app.route('/pernicky/<ID>', methods=['GET'])
def pernicky(ID):
    pernicky = databaza.pernicky1(ID)
    return render_template("pernicky.html", databaza=pernicky1, pernicky=pernicky)

@app.route('/pernicek8/')
def pernicek8():
    return render_template("pernicek8.html")

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

if __name__ == '__main__':
   app.debug = True
   app.run()
