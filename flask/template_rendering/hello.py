#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/lists')
def render_lists():
    # Soon enough, we'll get data from a database, but for now, we're hard coding data
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)


#@app.route('/foo') any other routes    
#def that_routes_foo():
    #return whatever

#this must be below ALL routes
if __name__=='__main__': 
    app.run(debug=True)










