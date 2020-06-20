from flask import Blueprint, request, Response, jsonify
from register.register import validate_admin_input, generate_hash, generate_salt, generate_jwt_token
from models.extensions import db
from models.models import Admin_Users
from datetime import datetime

admin_authentication = Blueprint("admin_authentication", __name__)

@admin_authentication.route("/login", methods=["POST"])
def login_admin():
    admin_email = request.json["email"]
    #htpp request, request content , json key value pairs, email is key, will the get value
    # admin = request.json["phone"]
    admin_password = request.json["password"]
    if (len(admin_email) != 0 and len(admin_password) != 0) :
        admin_record= Admin_Users.query.filter(Admin_Users.email == admin_email).first()
        if (admin_record):
            password_hash = generate_hash(admin_password, admin_record.password_salt)
            if (password_hash == admin_record.password_hash):
                admin_id = admin_record.id
                jwt_token = generate_jwt_token({"id": admin_id})
                return jsonify({"jwt_token": jwt_token})
            else:
                return  jsonify({"message": "Password incorrect"})
        else:
            return  jsonify({"message": "Admin_Users not found"})
    else:
        Response(status=400)

@admin_authentication.route("/register", methods = ["POST"])
def register_admin():
    data = request.get_json()
    error_message = validate_admin_input(data)
    if error_message:
        return Response(error_message, status = 400)
    else:
        admin_record = Admin_Users.query.filter(Admin_Users.email == data["email"]).first()
        if admin_record : return Response("Email already exists", 400)
        password_salt = generate_salt()
        password_hash = generate_hash(data["password"], password_salt)
        new_admin = Admin_Users(user_name=data["user_name"],
                             role=data["role"],
                             email=data["email"],
                             password_hash=password_hash,
                             password_salt=password_salt,
                             phone=data["phone"],
                             house=data["house"],
                             alias=data["alias"],
                             isActive= True,
                             created_date=datetime.now(),
                             created_by= data["created_by"])
        db.session.add(new_admin)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return Response(status=201)

@admin_authentication.route("/update", methods=["PUT"])
def update_admin():
        admin_id = request.json["id"]
        admin_email = request.json["email"]
        admin_phone = request.json["phone"]
        modified_by = request.json["modified_by"]
        if (((len(admin_email) != 0) or (len(admin_phone)!= 0)) and (len(admin_id)!=0) and (len(modified_by)!= 0)):
            admin_record = Admin_Users.query.filter(Admin_Users.id == admin_id).first()
            if not admin_record:
                return Response("Admin User not Found", status =400)
            else:
                admin_record.email = admin_email
                admin_record.phone = admin_phone
                admin_record.modified_date = datetime.now()
                admin_record.modified_by = modified_by
                db.session.commit()
                return Response(status = 200)
        else:
            return Response(status=400)
