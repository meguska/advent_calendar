from app import db
from sqlalchemy import Table, Column, Integer, String, MetaData

class Pernicky1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, index=True, unique=True)
    uloha = db.Column(db.String(250), index=True, unique=True)
    url = db.Column(db.String(120), index=True, unique=True)

   
  