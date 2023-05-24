from lib.db import db

class Article
  id = db.Column(db.Integer, primary_key= True, autoincrement=True)
  pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  name = db.Column(db.Text())
  article = db.Column(db.Text())

  def __init__(self, pub_date, name, article):
    self.pub_date = pub_date
    self.mame = name
    self.article = article