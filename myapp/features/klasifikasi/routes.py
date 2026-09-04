from apiflask import APIBlueprint, abort
from flask import url_for
from flask_jwt_extended import jwt_required, get_jwt_identity

# ----- repository -----
from myapp.features.klasifikasi.repository.klasifikasi_repository import KlasifikasiSuratRepository

# ----- schema -----
from myapp.features.klasifikasi import schema

klasifikasi_surat_bp = APIBlueprint("klasifikasi_surat", __name__, url_prefix="/klasifikasi_surat")

@klasifikasi_surat_bp.get("/kategori")
@klasifikasi_surat_bp.doc(security=[{"BearerAuth": []}])
@klasifikasi_surat_bp.output(schema.KategoriResponseSchema(many=True))
def kategori():
    kategori = KlasifikasiSuratRepository().get_by_surat()
    return kategori