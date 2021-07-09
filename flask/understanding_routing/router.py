#pipenv install flask ..... to make pipfile and pipfile.lock
#pipenv shell ..... to enter into shell
#python server.py ..... start your server
from flask import Flask

app = Flask(__name__)



# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes

@app.route('/dojo')
def success():
    return "Dojo!"


# app.run(debug=True) should be the very last statement!

@app.route('/say/<name>') 
def hello(name):
    print(name)
    return "Hi, " + name

@app.route('/repeat/<user_word>/<num>') 
def repeat(user_word, num):
    num = int(num)
    for num in range(0, num, 1):
        print(user_word)
    return f"{user_word}"


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.

# Create a server file that generates the specified responses for the following url requests:

# localhost:5000/ - have it say "Hello World!"x
# localhost:5000/dojo - have it say "Dojo!"x
# Create one url pattern and function that can handle the following examples:
# localhost:5000/say/flask - have it say "Hi Flask!"x
# localhost:5000/say/michael - have it say "Hi Michael!"x
# localhost:5000/say/john - have it say "Hi John!"x
# Create one url pattern and function that can handle the following examples (HINT: int() will come in handy! For example int("35") returns 35):
# localhost:5000/repeat/35/hello - have it say "hello" 35 times
# localhost:5000/repeat/80/bye - have it say "bye" 80 times
# localhost:5000/repeat/99/dogs - have it say "dogs" 99 times