import os
import oss2


def auth():
    accessKeyId = 'LTAI4GKxDucn4VBjKG8TS74V'
    accessKeySecret = 'KVsGpbnjTitjMmWvuvteV6MBDr8zW5'
    auth = oss2.Auth(accessKeyId, accessKeySecret)
    return auth


def endpoint():
    endpoint = 'https://oss-cn-beijing.aliyuncs.com'
    return endpoint


def create_bucket(user_id):
    bucketname = 'movie-share-{}'.format(user_id)
    bucket = oss2.Bucket(auth(), endpoint(), bucketname)
    bucket.create_bucket(oss2.BUCKET_ACL_PUBLIC_READ)
    return bucket


def select_bucket(user_id):
    bucketname = 'movie-share-{}'.format(user_id)
    bucket = oss2.Bucket(auth(), endpoint(), bucketname)
    return bucket

