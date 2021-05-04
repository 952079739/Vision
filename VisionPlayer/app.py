from flask import *
import flask_socketio
import os
from sockets import comment
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/' \
                                        'moviedata?charset=utf8mb4'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '123456'

db = SQLAlchemy(app)


from blueprints import play, users
app.register_blueprint(play.bp)
app.register_blueprint(users.user)


@app.route('/')
def index():
    return redirect(url_for("user.login"))


# socketio = flask_socketio.SocketIO(app)
socketio = flask_socketio.SocketIO(app, cors_allowed_origins="*")
comment.register_comment(socketio)

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80, debug=True, threaded='True')
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

