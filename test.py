from app import db
from create_db import User, Movie
from db_sql import *
from utils.movie_oss import create_bucket, select_bucket
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
# user_id = 1
# create_bucket(user_id)
# bucket = select_bucket(user_id)
# bucket.delete_bucket()
# filename = '/static/you/video/20210504221745.mp4'
# basepath = '/home/li/桌面/Vision'
# filepath = basepath + '20210504221745.mp4'
# name = '20210504221745.mp4'
# bucket.put_object_from_file(name, filepath)
# bucket.get_object_to_file(name, filepath)
