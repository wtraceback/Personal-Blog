from flask import render_template, redirect, flash, url_for
from flask_login import current_user, login_user, logout_user
from flask_login import login_required
from app.auth import auth_bp
from app.forms import LoginForm
from app.models import Admin


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('blog.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'warning')
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me.data)
        flash('Login successful', 'success')
        return redirect(url_for('blog.index'))
    return render_template('auth/login.html', form=form)


@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('blog.index'))
