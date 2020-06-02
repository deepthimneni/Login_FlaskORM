from flask import Blueprint, request, Response, jsonify
from register.register import validate_user_input, generate_hash, generate_salt, generate_jwt_token
from models.extensions import db
from models.models import User
from datetime import datetime

authentication = Blueprint("authentication", __name__)

@authentication.route("/login", methods=["POST"])
def login_user():
    user_email = request.json["email"]
    #htpp request, request content , json key value pairs, email is key, will the get value
    # user_phone = request.json["phone"]
    user_password = request.json["password"]
    if (len(user_email) != 0 and len(user_password) != 0) :
        user_record= User.query.filter(User.email == user_email).first()
        if (user_record):
            password_hash = generate_hash(user_password, user_record.password_salt)
            if (password_hash == user_record.password_hash):
                user_id = user_record.id
                jwt_token = generate_jwt_token({"id": user_id})
                return jsonify({"jwt_token": jwt_token})
            else:
                return  jsonify({"message": "Password incorrect"})
        else:
            return  jsonify({"message": "User not found"})
    else:
        Response(status=400)


@authentication.route("/register", methods=["POST"])
def register_user():
    user_email = request.json["email"]
    user_password = request.json["password"]
    user_confirm_password = request.json["confirm_password"]
    last_name = request.json["last_name"]
    first_name = request.json["first_name"]
    phone = request.json["phone"]
    dob = request.json["dob"]
    country = request.json["country"]
    gender = request.json["gender"]
    social_sites = request.json["social_sites"]
    bio = request.json["bio"]

    if user_password == user_confirm_password and validate_user_input(
        "authentication", email = user_email, password = user_password, phone = phone
    ):
        password_salt = generate_salt()
        password_hash = generate_hash(user_password, password_salt)
        dob = datetime.strptime(dob, "%m/%d/%Y")
        new_user = User(last_name=last_name,
                        first_name=first_name,
                        email=user_email,
                        password_hash=password_hash,
                        password_salt=password_salt,
                        phone=phone,
                        dob=dob,
                        country= country,
                        gender = gender,
                        social_sites = social_sites,
                        created = datetime.now(),
                        bio=bio,
                        admin=False)
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes

        return Response(status=201)

    else:
        return Response(status=400)

