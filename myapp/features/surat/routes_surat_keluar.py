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
from myapp.features.shared import schemas as shared_schemas

# ----- services -----
from myapp.features.surat import services


# ----- surat keluar -----
@surat_keluar_bp.get("/semua/") 
@surat_keluar_bp.doc(security=[{"BearerAuth": []}])
@surat_keluar_bp.input(schema.SuratSchema, location="query", arg_name="query_data")
@surat_keluar_bp.output(schema.PaginationSuratSchema(many=False))
# @jwt_required()
def semua_surat(query_data):
    data_request = query_data
    page = data_request.get("page", 1)
    page_size = data_request.get("page_size", 10)

    surat_repository = repository.surat_repository.SuratRepository()
    hasil = surat_repository.semua_surat(page=page, page_size=page_size)

    return hasil

@surat_keluar_bp.post("/tambah/")
@surat_keluar_bp.doc(
    summary="Tambah Surat Keluar",
    security=[{"BearerAuth": []}]
)
@surat_keluar_bp.input(schema.SuratKeluarModelSchemaRequest, location="json", arg_name="query_data")
@surat_keluar_bp.output(schema.paginationSuratKelurModelSchema(many=False))
def tambah(query_data):
    data = query_data
    
    res = services.surat_keluar_service.create(**data)
    if res.is_success:
        return res.data
    
    hasil = None
    return hasil

@surat_keluar_bp.get("/<int:surat_keluar_id>/lihat")
@surat_keluar_bp.doc(
    summary="Lihat Surat Keluar",
    security=[{"BearerAuth": []}],
    responses={
        400: {
            "description": "Surat Keluar Tidak Ditemukan",
            "content": {
                "application/json": {
                    "schema": shared_schemas.ErrorResponseSchema
                }
            }
        }
    }
)
@surat_keluar_bp.output(schema.SuratKeluarModelSchema(many=False))
def lihat(surat_keluar_id):
    result = services.surat_keluar_service.lihat(surat_keluar_id)
    hasil = result.data
    if result.is_success:
        return hasil
    return None

@surat_keluar_bp.post("/<int:surat_keluar_id>/hapus")
@surat_keluar_bp.doc(
    summary="Hapus Surat Keluar",
    security=[{"BearerAuth": []}],
    responses={
        200: {
          "description": "Surat Keluar Berhasil Dihapus",
          "content": {
              "application/json": {
                  "schema": shared_schemas.SuccessResponseSchema
              }
          }
        },
        204: {
            "description": "Surat Keluar Berhasil Dihapus",
            "content": {
                "application/json": {
                    "schema": shared_schemas.SuccessResponseSchema
                }
            }
        },
        400: {
            "description": "Surat Keluar Tidak Ditemukan",
            "content": {
                "application/json": {
                    "schema": shared_schemas.ErrorResponseSchema
                }
            }
        }
    }
)
def hapus(surat_keluar_id):
    result = services.surat_keluar_service.hapus(surat_keluar_id)
    
    if result.is_success:
        return {
            "message": result.message,
            "is_success": result.is_success,
        }
    return {
        "message": result.message,
        "is_success": result.is_success,
        "errors": {
            "message": result.message
        }
    }, 400

