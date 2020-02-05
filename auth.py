from flask import Blueprint,render_template,url_for
from flask import render_template,request,redirect,url_for
from models import db

auth = Blueprint('auth',__name__)

@auth.route("/")
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    user = AuthorityLogin.query.filter_by(Email = email).first()

    # if user 
    return render_template('input.html')

@auth.route("/",methods=['POST'])
def login_post():
    return render_template('input.html')

@auth.route("/logout")
def logout():
    return render_template(url_for('main.index'))