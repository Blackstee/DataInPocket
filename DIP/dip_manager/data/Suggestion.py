from mongoengine import *
import datetime


class Suggestion(Document):

    date_post = DateTimeField(default=datetime.datetime.utcnow)

    creator = ObjectIdField(required=False)

    text = StringField(max_length= 10000, required=True)

    photos = ListField(ImageField(), default=list)

    followers = ListField(ObjectIdField(), default=list)


    meta = {
        'db_alias': 'dip_pr_database',
        'collection': 'suggestions'
    }