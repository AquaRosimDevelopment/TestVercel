from flask import Blueprint, render_template, request, redirect, url_for, session

login_bp = Blueprint('login_bp', __name__)

VALID_USERNAME = 'admin'
VALID_PASSWORD = 'admin'

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['user'] = username
            return redirect(url_for('login_bp.protected'))

        return render_template('login.html', error="Invalid username or password")

    return render_template('login.html')

@login_bp.route('/protected')
def protected():
    if 'user' in session:
        return f"Welcome, {session['user']}! You are logged in."
    else:
        return redirect(url_for('login_bp.login'))

@login_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login_bp.login'))
