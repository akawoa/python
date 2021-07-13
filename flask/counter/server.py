from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "Yeet on em"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heroes', methods=['POST'])
def create_hero():
    session['name'] = 1
    session['alter_ego'] = request.form['alter_ego']
    session['catch_phrase'] = request.form['catch_phrase']
    return redirect('/')

@app.route('/success')
def success():
    if 'name' not in session:
        return redirect('/')  


@app.route('/logout')
def logout():
    del session['name']
    del session['alter_ego']
    del session['catch_phrase']

    # alternatively

    # session.clear() # this will clear EVERYTHING
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)