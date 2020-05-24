from dotenv import load_dotenv

import os

load_dotenv()

# MYSQL Config
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_PORT = os.getenv("MYSQL_PORT")

# JWT Config
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
