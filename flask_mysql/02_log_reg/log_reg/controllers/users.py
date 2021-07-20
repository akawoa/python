from log_reg import app
from flask import render_template, redirect, request, session
from log_reg.models.user import User

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    User.validate_registration