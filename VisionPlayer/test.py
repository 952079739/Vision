from app import db
from create_db import User, Movie
from db_sql import *
from utils.func import create

db.drop_all()
db.create_all()
# from utils.music_list import getMusic
#
# music_list = getMusic('static/upload')
# print(music_list)

# username = 'li'
# user = select_user_name(username)
# print(user)
# filepath = '/static/{}/uplode/'.format(username)
# msg = create(filepath)
# print(msg)

