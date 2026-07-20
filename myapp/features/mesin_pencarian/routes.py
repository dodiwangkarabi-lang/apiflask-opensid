from apiflask import APIBlueprint

# ----- auth -----
from flask_jwt_extended import jwt_required, get_jwt_identity

pencarian_bp = APIBlueprint(
    "pencarian",
    __name__,
    url_prefix="/pencarian"
)

@pencarian_bp.get("/")
@pencarian_bp.doc(security=[{"BearerAuth": []}])
@jwt_required()
def cari():
    username = get_jwt_identity()
    return {"message": "cari", "username": username}