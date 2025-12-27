from app import app
from flask import render_template, request
import app.db.user_db as users_db
@app.route('/')
def home(): 
    return render_template('homepage.html')

@app.route('/users' , methods=['POST'])
def users():
    users_db.register_user(request.form)
    return 'user is successfully created'
@app.route('/register')
def register():
    return 'Register Page'