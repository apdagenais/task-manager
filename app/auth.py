from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from app.models import User
from app.forms import LoginForm, RegisterForm

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already exists.', 'danger')
            return redirect(url_for('auth.login'))
        
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, email=form.email.data, password_hash=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash('Account created. You can log in.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(f"DEBUG: User found -> {user}")  # ✅ Check if user is found

        if user and user.password_hash and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=True)
            print(f"DEBUG: User logged in -> {user.username}")  # ✅ Check if user is logged in

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        
        flash('Invalid credentials, try again.', 'danger')
    
    print("DEBUG: Form not validated or incorrect credentials")  # ✅ Debug login failure
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

