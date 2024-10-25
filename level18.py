# Flask , Framework ringan dan sederhana
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Halo, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
