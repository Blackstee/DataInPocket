from mongoengine import *
import datetime


class Task(Document):

    task_name = StringField(required=True, max_length= 100)

    photos = ListField(ImageField(), default=list)

    description = StringField(max_length= 10000, required=True)

    date_start = DateTimeField(default=datetime.datetime.utcnow)

    date_end = DateTimeField(required=True)

    date_update = DateTimeField(default=datetime.datetime.utcnow)

    updated = IntField(required=False, default=0)

    creator = ObjectIdField(required=True)

    doer = ObjectIdField(required=True)

    comments = ListField(ObjectIdField(), default=list)

    followers = ListField(ObjectIdField(), default=list)



    meta = {
        'db_alias': 'dip_pr_database',
        'collection': 'tasks'
    }