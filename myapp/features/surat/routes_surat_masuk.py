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

surat_masuk_bp = APIBlueprint("surat-masuk", __name__, url_prefix="/api/surat-masuk")

# ----- skema -----
from .schema import CariSchema
from . import schema
from myapp.features.shared import schemas as shared_schemas

# ----- dto -----
from myapp.features.surat import dto


# ----- services -----
from myapp.features.surat import services

@surat_masuk_bp.get("/semua-surat/") 
@surat_masuk_bp.doc(security=[{"BearerAuth": []}])
@surat_masuk_bp.input(schema.SuratSchema, location="query", arg_name="query_data")
@surat_masuk_bp.output(schema.PaginationSuratSchema(many=False))
# @jwt_required()
def semua_surat(query_data):
    data_request = query_data
    page = data_request.get("page", 1)
    page_size = data_request.get("page_size", 10)

    surat_repository = repository.surat_repository.SuratRepository()
    hasil = surat_repository.semua_surat(page=page, page_size=page_size)

    return hasil

@surat_masuk_bp.post("/tambah/")
@surat_masuk_bp.doc(
    summary="Tambah Surat Masuk",
    security=[{"BearerAuth": []}]
)
@surat_masuk_bp.input(schema.SuratMasukModelSchemaRequest, location="json", arg_name="query_data")
@surat_masuk_bp.output(schema.PaginationSuratMasukModelSchema(many=False))
def tambah(query_data):
    # data = dto.SuratMasukDTO(**query_data)
    data = query_data
    
    res = services.surat_masuk_service.create(**data)
    if res.is_success:
        return res.data
    
    hasil = None
    return hasil

@surat_masuk_bp.get("/<int:surat_masuk_id>/lihat")
@surat_masuk_bp.doc(
    summary="Lihat Surat Masuk",
    security=[{"BearerAuth": []}],
    responses={
        400: {
            "description": "Surat Masuk Tidak Ditemukan",
            "content": {
                "application/json": {
                    "schema": shared_schemas.ErrorResponseSchema
                }
            }
        }
    }
)
@surat_masuk_bp.output(schema.SuratMasukModelSchema(many=False))
def lihat(surat_masuk_id):
    result = services.surat_masuk_service.lihat(surat_masuk_id)
    hasil = result.data
    if result.is_success:
        return hasil
    return None

@surat_masuk_bp.post("/<int:surat_masuk_id>/hapus")
@surat_masuk_bp.doc(
    summary="Hapus Surat Masuk",
    security=[{"BearerAuth": []}],
    responses={
        200: {
          "description": "Surat Masuk Berhasil Dihapus",
          "content": {
              "application/json": {
                  "schema": shared_schemas.SuccessResponseSchema
              }
          }
        },
        204: {
            "description": "Surat Masuk Berhasil Dihapus",
            "content": {
                "application/json": {
                    "schema": shared_schemas.SuccessResponseSchema
                }
            }
        },
        400: {
            "description": "Surat Masuk Tidak Ditemukan",
            "content": {
                "application/json": {
                    "schema": shared_schemas.ErrorResponseSchema
                }
            }
        }
    }
)
def hapus(surat_masuk_id):
    result = services.surat_masuk_service.hapus(surat_masuk_id)
    
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