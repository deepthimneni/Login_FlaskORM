import os
from hashlib import pbkdf2_hmac
import jwt
import re

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# validating user input
def validate_user_input(register_data):
    if not(register_data["email"]):
        return "Please enter email"
    elif not(register_data["password"]):
        return "Please enter password"
    elif not(register_data["confirm_password"]):
        return "Please confirm the password"
    elif register_data["password"] != register_data["confirm_password"]:
        return "Password does not Match, Try again!"
    elif not(register_data["last_name"]):
        return "Please enter Last Name"
    elif not(register_data["first_name"]):
        return "Please enter First Name"
    elif not(register_data["phone"]):
        return "Please enter Mobile Number"
    elif not(re.search(patterns["email"], register_data["email"])):
        return "Please enter a valid email"
    elif not(re.search(patterns["phone"], register_data["phone"])):
        return "Please enter a valid Mobile number"
    elif not(re.search(patterns["name"], register_data["first_name"])):
        return "Please enter valid First name"
    elif not (re.search(patterns["name"], register_data["last_name"])):
        return "Please enter valid Last name"
    else:
        return ""

# password salt technique
def generate_salt():
    salt = os.urandom(16)
    return salt.hex()

# password hash technique
def generate_hash(plain_password, password_salt):
    password_hash = pbkdf2_hmac(
        "sha256",
        b"%b" % bytes(plain_password, "utf-8"),
        b"%b" % bytes(password_salt, "utf-8"),
        10000,
    )
    return password_hash.hex()

#login password
def generate_jwt_token(content):
    encoded_content = jwt.encode(content, JWT_SECRET_KEY, algorithm="HS256")
    token = str(encoded_content).split("'")[1]
    return token

patterns = {
    "email" : '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
    "phone" : '(0/91)?[7-9][0-9]{9}',
    "name" : '^[a-zA-Z]+(( )*[a-zA-Z]+)*$'
}

#admin_function
def validate_admin_input(register_data):
    if not(register_data["email"]):
        return "Please enter email"
    elif not(register_data["password"]):
        return "Please enter password"
    elif not(register_data["confirm_password"]):
        return "Please confirm the password"
    elif register_data["password"] != register_data["confirm_password"]:
        return "Password does not Match, Try again!"
    elif not(register_data["user_name"]):
        return "Please enter User Name"
    elif not(register_data["phone"]):
        return "Please enter Mobile Number"
    elif not(register_data["alias"]):
        return "Please enter Alias"
    elif not(register_data["house"]):
        return "Please enter House name"
    elif not(register_data["created_by"]):
        return "Please enter who created"
    elif not(re.search(patterns["email"], register_data["email"])):
        return "Please enter a valid email"
    elif not(re.search(patterns["phone"], register_data["phone"])):
        return "Please enter a valid Mobile number"
    else:
        return ""