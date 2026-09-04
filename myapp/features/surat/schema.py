# from marshmallow import Schema, fields, validate
from apiflask import Schema, fields
from apiflask.fields import List, Nested
from myapp.core.pagination import BasePaginationSchema
from marshmallow import post_load, post_dump

# models
from myapp.features.surat import models

# class SuratPaginationSchema(BasePaginationSchema):
#     pass


def create_pagination_schema(item_schema):
    class PaginationSchema(Schema):
        data = fields.List(fields.Nested(item_schema))
        page = fields.Integer()
        page_size = fields.Integer()
        total = fields.Integer()
        total_pages = fields.Integer()

    return PaginationSchema

class HasilPencarianSuratSchema(Schema):
    id = fields.Integer()
    isi_singkat = fields.String()
    kode_surat = fields.String()
    tanggal_surat = fields.Date()
    berkas_scan = fields.String(allow_none=True)
    nomor_surat = fields.String()


class HasilPencarianSuratResponseSchema(Schema):
    id = fields.Integer()
    kemiripan = fields.Float()
    tipe_surat = fields.String(allow_none=True)
    surat = fields.Nested(HasilPencarianSuratSchema)

class CariSuratRequestSchema(Schema):
    keyword = fields.String(required=True)
    kode_surat = fields.String(required=False)
    nilai_kemiripan_min = fields.Float(load_default=0.5, allow_none=True)

class CariSchema(Schema):
    q = fields.String(required=False)
    page = fields.Integer(load_default=1)
    limit = fields.Integer(load_default=10)
    
class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    

# ----- surat masuk -----
class SuratMasukSchema(Schema):
    id = fields.Integer()
    nomor_urut = fields.Integer()
    # tanggal_penerimaan = fields.Date()
    nomor_surat = fields.String()
    kode_surat = fields.String()
    tanggal_surat = fields.Date()
    # perihal = fields.String()
    tujuan = fields.String()
    isi_singkat = fields.String()
    
    @post_load
    def create_surat(self, data, **kwargs):
        return models.SuratMasuk(**data)
    

# ----- surat keluar -----
class SuratKeluarSchema(Schema):
    id = fields.Integer()
    nomor_urut = fields.Integer()
    # tanggal_penerimaan = fields.Date()
    nomor_surat = fields.String()
    kode_surat = fields.String()
    tanggal_surat = fields.Date()
    # perihal = fields.String()
    tujuan = fields.String()
    isi_singkat = fields.String()
    
    @post_load
    def create_surat(self, data, **kwargs):
        return models.SuratKeluar(**data)
    

class SuratKeluarOrSuratMasuk(Schema):
    id = fields.Integer()
    kode_surat = fields.String()
    tanggal_surat = fields.Date()
    nomor_surat = fields.String()
    isi_singkat = fields.String()
    berkas_scan = fields.String()

class SuratSchema(BasePaginationSchema):
    id = fields.Integer()
    tipe_surat = fields.String(load_default=None, allow_none=True)
    surat = fields.Nested(SuratKeluarOrSuratMasuk, many=False) # tidak bisa gunakan  SuratMasuk or SuratKeluar
    # isi_singkat = fields.String()
    
    
    # kode_surat = fields.String(load_default=None, allow_none=True)
    # tanggal_surat = fields.Date(load_default=None, allow_none=True)
    # berkas_scan = fields.String(load_default=None, allow_none=True)
    # nomor_surat = fields.String(load_default=None, allow_none=True)
    
    

class PencarianSuratResponse(SuratSchema):
    kemiripan = fields.Float()
    
class QuerySchema(Schema):
    q = fields.String(required=False)
    page = fields.Integer(load_default=1)
    limit = fields.Integer(load_default=10)
    
    
class SuratKeluarPaginationSchema(BasePaginationSchema):
    count = fields.Integer()
    next = fields.String(allow_none=True)
    previous = fields.String(allow_none=True)
    results = fields.Nested(SuratKeluarSchema, many=True)
    
class HasilPencarianResponseSchema(Schema):
    id = fields.Integer()
    kemiripan = fields.Float()
    tipe = fields.String(
        load_default=None,
        allow_none=True
    )
    surat = fields.Nested(SuratSchema, many=False)
    
PaginationSuratSchema = create_pagination_schema(SuratSchema)