from flask import Flask, render_template
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)
            
if __name__ == "__main__":
    app.run(debug=True)