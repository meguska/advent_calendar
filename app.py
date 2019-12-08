from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    #print(get_activities)
    return render_template('index.html')

@app.route('/sdetmi/')
def sdetmi():
   return render_template("sdetmi.html")

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