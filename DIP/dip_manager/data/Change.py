from mongoengine import *
import datetime


class Change(Document):

    date_post = DateTimeField(default=datetime.datetime.utcnow)

    creator = ObjectIdField(required=True)

    act_type = StringField(required=True)

    before = ListField(default=list)

    after = ListField(default=list)

    meta = {
        'db_alias': 'dip_pr_database',
        'collection': 'changes'
    }