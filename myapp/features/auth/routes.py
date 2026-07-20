from apiflask import APIBlueprint

auth_bp = APIBlueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)

from flask_jwt_extended import (
    create_access_token, create_refresh_token
)
# from apiflask import request
from flask import request

# ----- schema -----
from apiflask import Schema
from apiflask.fields import String

class LoginSchema(Schema):
    username = String(required=True)
    password = String(required=True)
    
class TokenSchema(Schema):
    access = String()
    refresh = String()

@auth_bp.post("/login/")
@auth_bp.doc(security=[])
@auth_bp.input(LoginSchema)
@auth_bp.output(TokenSchema)
def login(json_data):
    data = json_data
    
    
    username = data["username"]
    password = data["password"]

    # Validasi user
    if username != "admin" or password != "admin":
        return {"message": "Username atau password salah"}, 401

    access_token = create_access_token(identity=username)
    refresh_token = create_refresh_token(identity=username)

    return {
        "refresh": refresh_token,
        "access": access_token
    }