import mongoengine


class User(mongoengine.Document):

    full_name = mongoengine.StringField(required=True)

    photo = mongoengine.ImageField(required=False)

    user_name = mongoengine.StringField(required=True)

    password = mongoengine.StringField(required=True)

    user_type = mongoengine.StringField(required=True)

    email = mongoengine.EmailField(required=True)

    user_telegram = mongoengine.StringField(required=False)




    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }