from inspect import classify_class_attrs
from . import db

class Properties_db(db.Model):
    __tablename__ = 'properties'

    