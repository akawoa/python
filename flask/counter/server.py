#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

app.secret_key = "Yeet on em"

@app.route('/')
def index():
    if 'counter' not in session:
        # then set sessions total gold value to be 0
        session['counter'] = 0
    session['counter'] += 1
    session.modified= True
    counter = session['counter']

    return render_template('index.html', counter=counter)

@app.route('/reset', methods=['POST'])
def reset():
    if request.form['button'] == "reset":
        session.pop('counter')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)