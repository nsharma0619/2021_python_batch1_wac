from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def welcomepage():
    return render_template('index.html', customer_name="neeraj")


@app.route("/profile/<name>")
def profile(name):
    return render_template('index.html', customer_name=name)

@app.route("/orders")
def orders():
    orders = ['pen', 'scale', 'rubber', 'sharpner']
    return render_template('order.html', orders=orders)


@app.route("/home")
def homepage():
    return "<h1>hello world second time</h1>"


if __name__ == "__main__":
    app.run(debug=True)