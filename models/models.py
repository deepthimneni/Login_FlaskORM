from models.extensions import db
import os
from sqlalchemy import *
import jwt

class User(db.Model):

    __tablename__ = 'sqlalchemy_demo_table'

    id = db.Column(db.Integer,
                   primary_key = True)
    first_name = db.Column(db.String(30),
                        index= True,
                        unique= False,
                        nullable= False)
    last_name = db.Column(db.String(30),
                           index=True,
                           unique=False,
                           nullable=False)
    password_hash = db.Column(db.String(255),
                           index= False,
                           unique= False,
                           nullable= False)
    password_salt = db.Column(db.String(255),
                          index=False,
                          unique=False,
                          nullable=False)
    email = db.Column(db.String(80),
                      index=True,
                      unique=True,
                      nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)
    gender = db.Column(db.String(15),
                       index = True,
                       unique = False,
                       nullable = False)
    dob = db.Column(db.Date,
                    index = False,
                    unique = False,
                    nullable = True)
    phone = db.Column(db.String(13),
                       index = False,
                       unique = False,
                       nullable = False)
    country = db.Column(db.String(20),
                       index = True,
                       unique = False,
                       nullable = False)
    bio = db.Column(db.Text,
                    index=False,
                    unique=False,
                    nullable=True)
    social_sites = db.Column(db.String(50),
                       index = False,
                       unique = False,
                       nullable = True)
    admin = db.Column(db.Boolean,
                      index=False,
                      unique=False,
                      nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.email)

