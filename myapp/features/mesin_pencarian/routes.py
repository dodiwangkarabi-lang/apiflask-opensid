from apiflask import APIBlueprint
from myapp.config import BASE_DIR

# ----- main -----
from myapp.features.mesin_pencarian import schema

# ----- use cases -----
from myapp.features.mesin_pencarian import usecases

# ----- service -----
from myapp.features.mesin_pencarian import services

# ----- repo -----
from myapp.features.surat import repository

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
    
# =====================================================
# buid model
# =====================================================
@pencarian_bp.get("/build-model/")
def build_model():
    uc_surat_keluar = usecases.BuildModelUC(tipe="surat_keluar")
    uc_surat_keluar.execute()
    
    uc_surat_masuk = usecases.BuildModelUC(tipe="surat_masuk")
    uc_surat_masuk.execute()
    
    return {"message": "model telah dibangun"}
    
@pencarian_bp.get("/cari-surat-masuk/")
@pencarian_bp.input(schema.PencarianRequestSchema, location="query")
@pencarian_bp.output(schema.HasilPencarianSchema(many=True))
@pencarian_bp.doc(security=[{"BearerAuth": []}])
# @jwt_required()
def cari_surat_masuk(query_data):
    repo = repository.SuratMasukRepository()
    
    # INDEX_DIR = BASE_DIR / "media" / "index"
    # search_engine_service = services.SearchEngine(
    #     index_file=INDEX_DIR / "index_surat_masuk.pkl"
    # )

    
    uc = usecases.SearchEngineUseCase(
        repo=repo,
        tipe="surat_masuk"
    )
    keyword = query_data["q"]
    hasil_pencarian = uc.search(keyword)
    
    return hasil_pencarian