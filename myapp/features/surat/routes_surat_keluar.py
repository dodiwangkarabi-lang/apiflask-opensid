from apiflask import APIBlueprint, abort
from flask import url_for

# ----- paginasi -----
from myapp.core.pagination import paginate

# ----- repository -----
from myapp.features.surat import repository

# ----- models -----
from myapp.features.surat import models

# ----- auth -----
from flask_jwt_extended import jwt_required, get_jwt_identity

surat_keluar_bp = APIBlueprint("surat-keluar", __name__, url_prefix="/api/surat-keluar")

# ----- skema -----
from .schema import CariSchema
from . import schema

# ----- services -----
from myapp.features.surat import services

@surat_keluar_bp.get("/semua-surat") 
@surat_keluar_bp.doc(security=[{"BearerAuth": []}])
# @surat_keluar_bp.input(schema.SuratKeluarSchema, location="query")
@surat_keluar_bp.output(schema.SuratKeluarSchema(many=False))
# @jwt_required()
def semua_surat():
    # data_request = query_data
    # page = data_request.get("page", 1)
    # page_size = data_request.get("page_size", 10)
    
    svc = services.surat_keluar_service
    hasil = svc.semua_surat()
    
    if hasil.is_success:
        return hasil.data.to_dict()
        # pass
    else:
        abort(400, message=hasil.message)

    # surat_repository = repository.surat_repository.SuratRepository()
    # hasil = surat_repository.semua_surat(page=page, page_size=page_size)

    # return hasil

