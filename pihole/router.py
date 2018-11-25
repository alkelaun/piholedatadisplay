from pihole.models import *

class DatabaseRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'pihole':
            return 'pihole'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'pihole':
            return 'pihole'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return (isinstance(obj1, FTL) == isinstance(obj2, FTL))

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'pihole':
            return False
        return True
