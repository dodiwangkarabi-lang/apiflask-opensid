from apiflask import APIBlueprint

# ----- main -----
from myapp.features.mesin_pencarian import schema
from myapp.features.mesin_pencarian import usecases

# ----- auth -----
from flask_jwt_extended import jwt_required, get_jwt_identity

pencarian_bp = APIBlueprint(
    "pencarian",
    __name__,
    url_prefix="/pencarian"
)

@pencarian_bp.get("/")
@pencarian_bp.input(schema.PencarianRequestSchema, location="query")
@pencarian_bp.output(schema.HasilPencarianSchema(many=True))
@pencarian_bp.doc(security=[{"BearerAuth": []}])
# @jwt_required()
def cari(query_data):
    uc = usecases.SearchEngineUseCase()
    keyword = query_data["q"]
    hasil_pencarian = uc.search(keyword)
    
    return hasil_pencarian
    
    # username = get_jwt_identity()
    # return {"message": "cari", "username": ""}