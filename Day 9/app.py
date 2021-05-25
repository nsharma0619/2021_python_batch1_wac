from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def welcomepage():
    return render_template('index.html')


@app.route("/home")
def homepage():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)