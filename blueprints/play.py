import json
from flask import *
from utils.func import random_name, file_extension, now
from utils.video_frame import capture
from utils.music_list import getMusic
from utils.movie_oss import select_bucket
from db_sql import *

bp = Blueprint('play', __name__, url_prefix="/play")


@bp.route('/upload', methods=['GET'])
def upload():
    return render_template('play/upload.html')


@bp.route('/music/upload', methods=['POST'])
def doupload():
    id = random_name()
    username = session['username']
    user_id = session['user_id']
    video = request.files['video']
    name = id + file_extension(video.filename)
    basepath = '/home/li/桌面/Vision'
    filename = 'static/{}/video/'.format(username) + name
    video.save(filename)
    filepath = basepath + '/' + filename
    bucket = select_bucket(user_id)
    bucket.put_object_from_file(name, filepath)
    add_movie(request.form["title"], name, user_id)

    # image = request.files['image']
    # image.save('static/image/' + id + file_extension(image.filename))

    image = 'static/image/' + id + '.jpg'
    capture('static/{}/upload/'.format(username) + id + file_extension(video.filename), image)

    data = {
        "author": request.form["author"],
        "date": now(),
        "image": "/" + image,
        "video": filename,
        "title": request.form["title"]
        # "description": request.form["description"]
    }
    with open("static/{}/upload/".format(username) + id + ".json", "w") as f:
        json.dump(data, f)

    return redirect(url_for('play.index_name', name=username))


@bp.route('/share', methods=['GET'])
def share():
    username = session['username']
    return jsonify({"msg": "127.0.0.1/play/{}".format(username)})


@bp.route('/<string:name>')
def index_name(name):
    username = name
    filepath = 'static/{}/upload'.format(username)
    music_list = getMusic(filepath)
    return render_template('play/player.html', musicList=music_list)


@bp.route('/')
def index():
    music_list = getMusic('static/upload')
    return render_template('play/player.html', musicList=music_list)