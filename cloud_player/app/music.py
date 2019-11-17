import os
import oss2

from flask import Blueprint, redirect, request, url_for, session, flash, render_template
from werkzeug.utils import secure_filename

import Oss
from app import db
from models import User

music = Blueprint('music', __name__)


@music.route('/index')
def index():
    return render_template('index.html')


@music.route('/upload', methods=['POST', 'GET'])
def music_upload():
    if request.method == 'GET':
        return render_template('upload.html')
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, 'music_storge', secure_filename(f.filename))
        f.save(upload_path)
        bucket = oss2.Bucket(Oss.auth(), Oss.endpoint(), 'li-{}-music'.format('wen'))
        bucket.put_object_from_file(f.filename,
                                    '/home/li/桌面/cloud_player/app/music_storge/{}'.format(f.filename))
        return redirect(url_for('music.index'))


@music.route('/search', methods=['POST', 'GET'])
def search():
    if request.methd == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        user_id = request.form['user_id']
        user = db.session.query(User).filter(User.id == user_id).one()
        username = Oss.get_name(user.username)
        bucket = Oss.get_bucket(username)












