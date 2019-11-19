import oss2
from flask import session

from app import db
from app.models import User


def auth():
    accessKeyId = 'LTAI4FevVcxQBxb5pARFFMUR'
    accessKeySecret = '9CxSxQsAfgKoXhKCFVy6nY2vNBY2PJ'
    auth = oss2.Auth(accessKeyId, accessKeySecret)
    return auth


def endpoint():
    endpoint = 'http://oss-cn-shanghai.aliyuncs.com'
    return endpoint


def create_bucket(bucketname):
    bucket = oss2.Bucket(auth(), endpoint(), bucketname)
    bucket.create_bucket(oss2.models.BUCKET_ACL_PUBLIC_READ)
    return bucket


def get_name(name):
    bucketname = 'li-{}-music'.format(name)
    return bucketname


def get_bucket(user_id):
    user = db.session.query(User).filter(User.id == user_id).one()
    username = get_name(user.username)
    bucket = oss2.Bucket(auth(), endpoint(), username)
    return bucket

