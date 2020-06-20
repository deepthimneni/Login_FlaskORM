from models.extensions import db
import os
from sqlalchemy import *
import jwt
db.metadata.clear()

class B2C_Users(db.Model):

    __tablename__ = 'tbl_b2c_users'
    __table_args__ = {'extend_existing': True}

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
    def __repr__(self):
        return '<B2C_Users {}>'.format(self.email)



class Admin_Users(db.Model):

    __tablename__ = 'tbl_admin_users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer,
                       primary_key=True)
    role = db.Column(db.Integer,
                     #index=True,
                     default=0,
                     #server_default=0,
                     nullable = False)
    user_name = db.Column(db.String(50),
                          index=True,
                          unique=False,
                          nullable=False)
    password_hash = db.Column(db.String(255),
                                  index=False,
                                  unique=False,
                                  nullable=False)
    password_salt = db.Column(db.String(255),
                                  index=False,
                                  unique=False,
                                  nullable=False)
    email = db.Column(db.String(80),
                          index=True,
                          unique=True,
                          nullable=False)
    alias = db.Column(db.String(15),
                           index=False,
                           unique=True,
                           nullable=False)
    phone = db.Column(db.String(13),
                          index=False,
                          unique=False,
                          nullable=False)
    house = db.Column(db.String(20),
                            index=True,
                            unique=False,
                            nullable=False)
    isActive = db.Column(db.Boolean,
                        index=False,
                        unique=False,
                        nullable=True)
    created_date = db.Column(db.DateTime,
                            index=False,
                            unique=False,
                            nullable=False)
    created_by = db.Column(db.String(40),
                             index= True,
                             unique= False,
                             nullable= False)
    modified_date = db.Column(db.Date,
                                 index=False,
                                 unique=False,
                                 nullable=True)
    modified_by = db.Column(db.String(40),
                             index= True,
                             unique= False,
                             nullable= True)
    def __repr__(self):
        return '<Admin_Users {}>'.format(self.email)