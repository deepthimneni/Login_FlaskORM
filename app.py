from flask import Flask
from utils.settings import MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB, MYSQL_HOST
from authentication.blueprint_auth import authentication
from utils.extensions import db

app = Flask(__name__)

app.config["MYSQL_USER"] = MYSQL_USER
app.config["MYSQL_PASSWORD"] = MYSQL_PASSWORD
app.config["MYSQL_DB"] = MYSQL_DB
app.config["MYSQL_HOST"] = MYSQL_HOST
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

app.register_blueprint(authentication, url_prefix="/api/auth")

db.init_app(app)
