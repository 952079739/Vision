import oss2
#
# from itertools import islice
#
from sqlalchemy.orm import session

import Oss
from app import db
from app.models import User


class test():
    # username = 'wen'
    # name = 'li-{}-music'.format(username)
    # bucket = oss2.Bucket(Oss.auth(), Oss.endpoint(), name)
    # for b in oss2.ObjectIterator(bucket)
    #     print(b.key)
    # username = 'wen'
    # password = '123456'
    # user = db.session.query(User).filter(User.id == 1).one()
    # print(user.id)
    # db.session.close()
    # name = 'li-wen-music'
    # bucket = oss2.Bucket(Oss.auth(), Oss.endpoint(), name)
    # bucket.put_object_from_file('你好.mp3', '/home/li/桌面/你好.mp3')
    bucket = Oss.get_bucket(1)
    url = bucket.sign_url('GET', 'music-two.mp3', 60)
    print(url)