from flask import render_template,request
from flask_login import login_user, login_required, logout_user, current_user

@login_required
def home():
    try:
        return render_template('home.html')
    except Exception as error:
        return error