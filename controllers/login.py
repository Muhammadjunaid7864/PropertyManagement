from flask import render_template, redirect, url_for, flash, request,jsonify
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from models.user import User


def login():
    try:
        if request.method == 'POST':
            data = request.get_json()  # Get JSON data
            username = data.get('username')
            password = data.get('password')
            user = User.query.filter_by(username=username).first()

            if user and user.password == password:
                login_user(user)
                return jsonify({'status': 'success', 'message': 'Login Successfully'}),200
            else:
                return jsonify({'status': 'error', 'message':'Login unscessfully, Please check username and password'}),401

        return render_template('login.html')
    except Exception as error:
        return jsonify({'status':'error','message': str(error)}),501


@login_required
def logout():
    logout_user()
    return redirect(url_for('app_bp.login'))


