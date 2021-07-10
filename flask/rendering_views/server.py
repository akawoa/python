from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # notice the 2 new named arguments!
    return render_template("index.html", phrase="hello", times=5)


if __name__ == "__main__":
    app.run(debug=True)
