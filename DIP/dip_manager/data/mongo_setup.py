import mongoengine


def global_init():
    mongoengine.register_connection(name='dip_project')
