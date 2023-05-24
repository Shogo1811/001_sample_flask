from flask import Flask, request, render_template
from datetime import datetime
from flask_sqalchemy import SQQLAlchemy
app = Flask(__name__)

class Article(db.Model):
  id = db.Column(db.Integer, primary_key=True, autincrement=True)
  pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utnow)
  name = db.Column(db.Text())
  article = db.Column(db.Text())


@app.route('/')
def bbs():
  message = 'Hello'
  return render_template('index.html', message = message)

if __name__ == "__main__":
  app.run(debug=True)

