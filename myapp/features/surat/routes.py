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

surat_bp = APIBlueprint(
    "surat",
    __name__,
    url_prefix="/surat"
)

# ----- skema -----
from .schema import CariSchema
from . import schema

@surat_bp.get("/cari")
@surat_bp.doc(security=[{"BearerAuth": []}])
@surat_bp.input(CariSchema, location="query")
# @jwt_required()
def cari(query_data):
    # username = get_jwt_identity()
    
    return {
        "message": "cari", 
        # "username": username,
        "query": query_data
    }
    
# ----- detail surat keluar -----
@surat_bp.get("/surat-keluar/<int:surat_keluar_id>/")
@surat_bp.output(schema.SuratKeluarSchema)
@surat_bp.doc(security=[{"BearerAuth": []}])
# @jwt_required()
def detail_surat_keluar(surat_keluar_id):
    try:
        surat_keluar = models.SuratKeluar.query.get_or_404(surat_keluar_id)
    except:
        abort(404)
    
    return surat_keluar
    
@surat_bp.get("/surat-keluar/")
@surat_bp.doc(security=[{"BearerAuth": []}])
@surat_bp.input(schema.QuerySchema, location="query") # patokannya adalah location=query (GET | POST | FORMDATA)
@surat_bp.output(schema.SuratKeluarPaginationSchema)
# @jwt_required()
def surat_keluar(query_data):
    # username = get_jwt_identity()
    params = query_data
    surat_masuk_repo = repository.SuratKeluarRepository()
    
    # ----- helpers -----
    def cari(query, keyword):
        if keyword:
            query = query.filter(
                models.SuratKeluar.isi_singkat.like(f"%{keyword}%")
            )
        return query
    
    # surat_keluar_qs = surat_masuk_repo.get_all()
    surat_keluar_qs = models.SuratKeluar.query
    
    # ----- pencarian -----
    if params.get("q"):
        keyword = f"%{params['q']}%"
        surat_keluar_qs = surat_keluar_qs.filter(
            models.SuratKeluar.isi_singkat.like(keyword)
        )
    
    
    # ----- paginasi -----
    pagination = surat_keluar_qs.paginate(
        page = params["page"],
        per_page = params["limit"],
        error_out=False
    )
    
    
    
    # return surat_keluar_qs
    # return surat_keluar_qs
    
    next_url = None
    prev_url = None
    
    if pagination.has_next:
        next_url = url_for("surat.surat_keluar", page=pagination.next_num, per_page=params["limit"], _external=True)
        
    if pagination.has_prev:
        prev_url = url_for("surat.surat_keluar", page=pagination.prev_num, per_page=params["limit"], _external=True)
        
    
    
    return {
        "count": pagination.total,
        "next": next_url,
        "previous": prev_url,
        "results": pagination.items
    }
    