from flask import Blueprint, request, Response, jsonify
from register.register import validate_user_input, generate_hash, generate_salt, generate_jwt_token, patterns
from models.extensions import db
from models.models import B2C_Users
from datetime import datetime

authentication = Blueprint("authentication", __name__)

@authentication.route("/login", methods=["POST"])
def login_user():
    user_email = request.json["email"]
    #htpp request, request content , json key value pairs, email is key, will the get value
    # user_phone = request.json["phone"]
    user_password = request.json["password"]
    if (len(user_email) != 0 and len(user_password) != 0) :
        user_record= B2C_Users.query.filter(B2C_Users.email == user_email).first()
        if (user_record):
            password_hash = generate_hash(user_password, user_record.password_salt)
            if (password_hash == user_record.password_hash):
                user_id = user_record.id
                jwt_token = generate_jwt_token({"id": user_id})
                return jsonify({"jwt_token": jwt_token})
            else:
                return  jsonify({"message": "Password incorrect"})
        else:
            return  jsonify({"message": "B2C_Users not found"})
    else:
        Response(status=400)


@authentication.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()

    error_message = validate_user_input(data)

    if error_message :
        return Response(error_message, status = 400)
    else:
        user_record= B2C_Users.query.filter(B2C_Users.email == data["email"]).first()
        if user_record: return Response("Email already exists", 400)

        password_salt = generate_salt()
        password_hash = generate_hash(data["password"], password_salt)
        new_user = B2C_Users(last_name=data["last_name"],
                        first_name=data["first_name"],
                        email=data["email"],
                        password_hash=password_hash,
                        password_salt=password_salt,
                        phone=data["phone"],
                        dob=datetime.strptime(data["dob"], "%m/%d/%Y"),
                        country= data["country"],
                        gender = data["gender"],
                        social_sites = data["social_sites"],
                        created = datetime.now(),
                        bio=data["bio"])
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return Response(status=201)

@authentication.route("/update", methods=["PUT"])
def update_user():
        user_id = request.json["id"]
        user_email = request.json["email"]
        user_phone = request.json["phone"]
        if (((len(user_email) != 0) or (len(user_phone)!= 0)) and (len(user_id)!=0)):
            user_record = B2C_Users.query.filter(B2C_Users.id == user_id).first()
            user_record.email = user_email
            user_record.phone = user_phone
            db.session.commit()
            return Response(status = 200)
        else:
            return Response(status=400)

