import os
import oss2

from flask import Blueprint, redirect, request, url_for, session, render_template
from werkzeug.utils import secure_filename

import Oss
from app import db
from app.models import User

music = Blueprint('music', __name__)


@music.route('/index')
def index():
    user_id = session.get('user_id')
    user = db.session.query(User).filter(User.id == user_id).one()
    username = user.username
    bucket = Oss.get_bucket(user_id)
    music_list = []
    for b in oss2.ObjectIterator(bucket):
        if b is not None:
            name = b.key
            music_url = bucket.sign_url('GET', name, 60*60)
            music_list.append({'name': name,
                               'music_url': music_url})
    return render_template('index.html', username=username, musics=music_list)


@music.route('/upload', methods=['POST', 'GET'])
def music_upload():
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'music_storge', f.filename)
        f.save(upload_path)
        user_id = session.get('user_id')
        bucket = Oss.get_bucket(user_id)
        bucket.put_object_from_file(f.filename, upload_path)
        return redirect(url_for('music.index'))


@music.route('/search', methods=['POST', 'GET'])
def serach_id():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        user_name = request.form['user_name']
        user = db.session.query(User).filter(User.username == user_name).one()
        user_id = user.id
        session.clear()
        session['user_id'] = user_id
        return redirect(url_for('music.index'))












