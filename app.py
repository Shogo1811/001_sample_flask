from flask import Flask, request, render_temple
from datetime import datetime
from flask_sqlalchemy import flask_sqlalchemy
app = Flask(__name__)

db_kane = 
app.config[] = db_kane
db = SQLAlchemy(app)

class Article(db.Model):
  id = db.Column(db.Integer, primary_key= True, autoincrement=True)
  pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  name = db.Column(db.Text())
  article = db.Column(db.Text())

@app.route('/')
def writing():
    text = Article.query.all()
    return render_template('index.html', lines = text)
  
@app.route('/result', methods=['POST'])
def result():
    data = datatime.now()
    article = request.form['article']
    name = request.form['name']
    admin = Article(pub_date=date, name=name, article=article)
    db.session.add(admin)
    db.session.commit()
    return render_template('result.html', article=article, name=name, now=data)
    
if __name__ == "__main__":
    app.run(debug=True)

