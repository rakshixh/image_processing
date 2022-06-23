from flask import Flask, render_template

app = Flask(__name__)


@app.route("/developer")
def developer():
    return render_template("developer.html")


if __name__ == '__main__':

    app.run(debug=True)