from inspect import classify_class_attrs
from . import db
class Properties_db(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    property_name = db.Column(db.String(80))
    description = db.Column(db.String(255))
    rooms_num = db.Column(db.Integer)
    bathrooms_num = db.Column(db.Integer)
    price = db.Column(db.Integer)
    property_type = db.Column(db.String(9))
    location = db.Column(db.String(255))
    photo = db.Column(db.String(80))

    def __init__(self,property_name,description,rooms_num,bathrooms_num,price,property_type,location,photo):
        self.property_name = property_name
        self.description = description
        self.rooms_num = rooms_num
        self.bathrooms_num = bathrooms_num
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo = photo

    def __repr__(self):
        return '<property %r %r %r %r %r %r %r %r>' % (self.property_name, self.description, self.rooms_num, self.bathrooms_num,self.price,self.property_type,self.location,self.photo)