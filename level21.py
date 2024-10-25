from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', nama="Indra")




@app.route('/profile')
def profile():
    return "This is your profile"




if __name__ == '__main__':
    app.run(debug=True)