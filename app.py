from flask import Flask

app = Flask(__name__)

@app.route('/')
def index(word=None):
    if word:
      return word
    else:
      return 'Hello World'

if __name__ == "__main__":
    app.run(debug=True)

