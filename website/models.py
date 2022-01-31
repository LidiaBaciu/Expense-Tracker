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
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    created = db.Column(db.DateTime(timezone=True), default=func.now())
    birthday = db.Column(db.DateTime(timezone=True))
    addresses = db.relationship('Address', secondary=user_address_table)
    incomes = db.relationship('Income')
    # spendings = db.relationship('Spending')
    

class IncomeType(db.Model):
    __tablename__ = 'incomeType'
    id = db.Column(db.Integer, primary_key=True)
    income_name = db.Column(db.String(150))
    
    
class Income(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True), default=func.now())
    amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    income_type_id = db.Column(db.Integer, db.ForeignKey('incomeType.id'))
   

class SpendingType(db.Model):   
    __tablename__ = 'spendingType'
    id = db.Column(db.Integer, primary_key=True)
    spending_name = db.Column(db.String(150))
    goal = db.Column(db.Float)
    

class SpendingCategory(db.Model):
    __tablename__ = 'spendingCategory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    description = db.Column(db.String(150))
    

class Spending(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True), default=func.now())
    amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    spending_type_id = db.Column(db.Integer, db.ForeignKey('spendingType.id'))
    spending_category_id = db.Column(db.Integer, db.ForeignKey('spendingCategory.id'))
  
  
class SavingType(db.Model):   
    __tablename__ = 'savingType'
    id = db.Column(db.Integer, primary_key=True)
    saving_type = db.Column(db.String(150))
    goal = db.Column(db.Float)
      

class Saving(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(timezone=True), default=func.now())
    amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    saving_type_id = db.Column(db.Integer, db.ForeignKey('savingType.id'))
