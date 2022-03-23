from inspect import classify_class_attrs
from . import db

class Properties_db(db.Model):
    __tablename__ = 'properties'

    property_name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    rooms_num = db.Column(db.Integer)
    bathrooms_num = db.Column(db.Integer)
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(9))
    location = db.Column(db.String(255))
    image_file = db.Column(db.String(20))

    def __init__(self,property_name,description,rooms_num,bathrooms_num,price,property_type,location,image_file):
        self.property_name = property_name
        self.description = description
        self.rooms_num = rooms_num
        self.bathrooms_num = bathrooms_num
        self.price = price
        self.property_type = property_type
        self.location = location
        self.image_file = image_file