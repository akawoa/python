from flask import Flask, render_template, request, redirect
from datetime import datetime 
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    now = datetime.now()
    print("now =", now)
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    

    print(request.form)
    strawberry = int(request.form['strawberry'])
    raspberry = int(request.form['raspberry'])
    apple = int(request.form['apple'])
    blackberry = int(request.form['blackberry'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    total_items = strawberry + raspberry + apple + blackberry

    return render_template("checkout.html", strawberry = strawberry,raspberry = raspberry,apple = apple,blackberry = blackberry,first_name = first_name,last_name = last_name,student_id = student_id,total_items = total_items, date = dt_string)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    