# Your program should have the following output

# http://localhost:5000 - should display 8 by 8 checkerboard
# http://localhost:5000/4 - should display 8 by 4 checkerboard
# http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)
# HINT: Remember that values from urls come in as strings by default. If you want to use the value in a loop, you should convert it to an integer before passing it to Jinja.

# pipenv install flask ..... to make pipfile and pipfile.lock
# pipenv shell ..... to enter into shell
# python server.py ..... start your server
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def checkerboard():
    return render_template('index.html')
# @app.route('/foo') any other routes
# def that_routes_foo():
    # return whatever

@app.route('/4')
def width_four():
    return render_template('index2.html')


@app.route('/<x>/<color>')
def variable_width(x, color):
    user_input1 = int(x)
    user_input2 = color
    return render_template('index3.html', width = user_input1,color=user_input2)


@app.route('/<x>/<y>')
def variable_length_width(x, y):
    user_input1 = int(x)
    user_input2 = int(y)
    return render_template('index4.html',  width = user_input1,  height = user_input2)


# this must be below ALL routes
if __name__ == '__main__':
    app.run(debug=True)
