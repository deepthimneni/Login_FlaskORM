from flask import Flask
from api.authentication_api import authentication
from api.admin_authentication_api import admin_authentication
from models.extensions import db
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

# MYSQL Config- Variables Declaring, Initializing
# MYSQL_USER = os.getenv("MYSQL_USER")
# MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
# MYSQL_DB = os.getenv("MYSQL_DB")
# MYSQL_HOST = os.getenv("MYSQL_HOST")
# MYSQL_PORT = os.getenv("MYSQL_PORT")

# JWT Config

# Using Variables
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False
# app.config["MYSQL_USER"] = os.getenv("MYSQL_USER")
# app.config["MYSQL_PASSWORD"] = os.getenv("MYSQL_PASSWORD")
# app.config["MYSQL_DB"] = os.getenv("MYSQL_DB")
# app.config["MYSQL_HOST"] = os.getenv("MYSQL_HOST")
# app.config["MYSQL_PORT"] = int(os.getenv("MYSQL_PORT"))
# app.config["MYSQL_CURSORCLASS"] = "DictCursor"

app.register_blueprint(authentication, url_prefix="/api/auth_user")
#modular_development
#app flask
#arguments1 - authentication
#arguments2- url_prefix
app.register_blueprint(admin_authentication, url_prefix = "/api/auth_admin")

db.init_app(app)

with app.app_context():
    db.create_all()

