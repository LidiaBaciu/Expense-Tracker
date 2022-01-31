from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


user_address_table = db.Table('user_address_table',
                              db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                              db.Column('address_id', db.Integer, db.ForeignKey('address.id')))


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(150))
    street_no = db.Column(db.Integer)
    city = db.Column(db.String(150))
    country = db.Column(db.String(150))
    # users = db.relationship('User', secondary=user_address_table)
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    created = db.Column(db.DateTime(timezone=True), default=func.now())
    birthday = db.Column(db.DateTime(timezone=True))
    addresses = db.relationship('Address', secondary=user_address_table)