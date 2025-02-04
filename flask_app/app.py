from flask import Flask,render_template



app = Flask(__name__)



@app.route("/")
def openpage():
    return render_template('base.html')


@app.route("/Home")
def homepage():
    return render_template('base.html')
@app.route("/About")
def About():
    return render_template('about.html')
@app.route("/Portfolio")
def portfolio():
    return render_template('portfolio.html')


if __name__ == '__main__':
    app.run(debug=True)

