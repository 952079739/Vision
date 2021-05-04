import json
from flask import *
from utils.func import random_name, file_extension, now
from utils.video_frame import capture
from utils.music_list import getMusic

bp = Blueprint('play', __name__, url_prefix="/play")


@bp.route('/upload', methods=['GET'])
def upload():
    return render_template('play/upload.html')


@bp.route('/music/upload', methods=['POST'])
def doupload():
    id = random_name()
    username = session['username']
    video = request.files['video']
    video.save('static/{}/video/'.format(username) + id + file_extension(video.filename))

    # image = request.files['image']
    # image.save('static/image/' + id + file_extension(image.filename))

    image = 'static/image/' + id + '.jpg'
    capture('static/{}/upload/'.format(username) + id + file_extension(video.filename), image)

    data = {
        "author": request.form["author"],
        "date": now(),
        "image": "/" + image,
        "video": "/static/{}/video/".format(username) + id + file_extension(video.filename),
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