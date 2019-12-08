from app import db

class Pernicky(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, unique=True)
    uloha = db.Column(db.String(250), index=True, unique=True)

   
  