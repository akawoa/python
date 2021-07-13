#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "Final Fantasy"

@app.route('/')
def foo():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def create():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def success():
    if 'name' not in session:
        return redirect('/')
    return render_template('result.html')

#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)