#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template, redirect, session, request
import random
from datetime import datetime 
app = Flask(__name__)
app.secret_key = "secret"


@app.route('/')
def foo():
    if 'total_gold' not in session:
        # then set sessions total gold value to be 0
        session['total_gold'] = 0
        session['activities'] = []
    total_gold = session['total_gold']
    activities = session['activities']
    return render_template('index.html', total_gold=total_gold,activities=activities)
#@app.route('/foo') any other routes    
#def that_routes_foo():
    #return whatever

@app.route('/process_money', methods=['POST'])
def process_money():
    print('test')
    if request.form['building'] == "farm":
        mystery = random.randint(10,20)
        session['total_gold'] += mystery
        session.modified = True
        now = datetime.now()
        print("now =", now)
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        session['activities'].append(f"Earned {mystery} gold from the farm! {dt_string}")
    if request.form['building'] == "cave":
        mystery = random.randint(5,10)
        session['total_gold'] += mystery
        session.modified = True
        now = datetime.now()
        print("now =", now)
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        session['activities'].append(f"Earned {mystery} gold from the cave! {dt_string}")
    if request.form['building'] == "house":
        mystery = random.randint(2,5)
        session['total_gold'] += mystery
        session.modified = True
        now = datetime.now()
        print("now =", now)
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        session['activities'].append(f"Earned {mystery} gold from the house! {dt_string}")
    if request.form['building'] == "casino":
        mystery = random.randint(-50,50)
        session['total_gold'] += mystery
        session.modified = True
        now = datetime.now()
        print("now =", now)
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        if mystery >= 0:
            session['activities'].append(f"Earned {mystery} gold from the casino! {dt_string}")
        else:
            session['activities'].append(f"Lost {mystery} gold from the casino! {dt_string}")
    return redirect ('/')

#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)