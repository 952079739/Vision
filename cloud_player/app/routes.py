from app import app
from app.user import user
from app.music import music


app.register_blueprint(user, url_prefix='/')
app.register_blueprint(music, url_prefix='/music')