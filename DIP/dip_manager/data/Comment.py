from mongoengine import *
import datetime


class Comment(Document):

    creator = ObjectIdField(required=True)

    text = StringField(max_length= 1000, required=True)

    photos = ListField(ImageField(), default=list)

    date_post = DateTimeField(default=datetime.datetime.utcnow)

    date_update = DateTimeField(default=datetime.datetime.utcnow)

    updated = IntField(required=False, default=0)

    followers = ListField(ObjectIdField(), default=list)


    meta = {
        'db_alias': 'dip_pr_database',
        'collection': 'comments'
    }