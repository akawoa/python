from flask_app import app,render_template,redirect,request,session
from flask_app.controllers import burgers

from mysqlconnection import connectToMySQL


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/create',methods=['POST'])
def create():
    query = "INSERT INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES (%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW())"
    data = {
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }

    mysql = connectToMySQL('burgers')
    mysql.query_db(query,data)
    return redirect('/burgers')




@app.route('/burgers')
def burgers():
    query = "SELECT * FROM burgers;"
    burgers = connectToMySQL('burgers').query_db(query)
    return render_template("results.html",all_burgers=burgers)


@app.route('/show/<int:burger_id>')
def detail_page(burger_id):
    query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
    data = {
        'id': burger_id
    }
    results = connectToMySQL('burgers').query_db(query,data)
    
    return render_template("details_page.html",burger=results[0])

@app.route('/edit_page/<int:burger_id>')
def edit_page(burger_id):
    query = "SELECT * FROM burgers WHERE id = %(id)s;"
    data = {
        'id': burger_id
    }
    burger = connectToMySQL('burgers').query_db(query,data)
    print(burger)
    return render_template("edit_page.html", burger = burger[0])

@app.route('/update/<int:burger_id>', methods=['POST'])
def update(burger_id):
    query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s,updated_at = NOW() WHERE id = %(id)s;"
    data = {
        'id': burger_id,
        "name":request.form['name'],
        "bun": request.form['bun'],
        "meat": request.form['meat'],
        "calories": request.form['calories']
    }
    burger = connectToMySQL('burgers').query_db(query,data)
    print(burger)
    return redirect(f"/show/{burger_id}")

@app.route('/delete/<int:burger_id>')
def delete(burger_id):
    query = "DELETE FROM burgers WHERE id = %(id)s;"
    data = {
        'id': burger_id,
    }
    connectToMySQL('burgers').query_db(query,data)
    return redirect('/burgers')

if __name__=="__main__":
    app.run(debug=True)