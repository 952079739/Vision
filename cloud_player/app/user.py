import functools

from flask import Blueprint, redirect, request, url_for, session, flash, render_template
from app import db
from app.models import User
import Oss

user = Blueprint('user', __name__)


@user.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST':
        p_user = request.form.get('username', None)
        p_password = request.form.get('password', None)

        if not p_user or not p_password:
            return 'input error'

        newobj = User(username=p_user, password=p_password)
        db.session.add(newobj)
        db.session.commit()
        name = 'li-{}-music'.format(p_user)
        Oss.create_bucket(name)
        return redirect(url_for('user.login'))


@user.route('/')
@user.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.session.query(User).filter(User.username == username, User.password == password).one()
        if user is not None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('music.index'))



