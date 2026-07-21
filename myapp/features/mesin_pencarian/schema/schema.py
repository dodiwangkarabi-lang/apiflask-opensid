# from marshmallow import Schema, fields, validate
from apiflask import Schema, fields
from apiflask.fields import List, Nested
from myapp.core.pagination import BasePaginationSchema
from marshmallow import post_load, post_dump



class DocumentSchema(Schema):
    id = fields.Integer()
    nomor_urut = fields.Integer()
    # tanggal_penerimaan = fields.Date()
    nomor_surat = fields.String()
    kode_surat = fields.String()
    tanggal_surat = fields.Date()
    lokasi_arsip = fields.String()
    isi_singkat = fields.String()
    
class HasilPencarianSchema(Schema):
    score = fields.Float()
    document = Nested(DocumentSchema)


class PencarianRequestSchema(Schema):
    q = fields.String(load_default="")
    

# # models
# from myapp.features.surat import models


# class CariSchema(Schema):
#     q = fields.String(required=False)
#     page = fields.Integer(load_default=1)
#     limit = fields.Integer(load_default=10)
    
# class UserSchema(Schema):
#     id = fields.Integer()
#     name = fields.String()
    

# # ----- surat keluar -----
# class SuratKeluarSchema(Schema):
#     id = fields.Integer()
#     nomor_urut = fields.Integer()
#     tanggal_penerimaan = fields.Date()
#     nomor_surat = fields.String()
#     kode_surat = fields.String()
#     tanggal_surat = fields.Date()
#     perihal = fields.String()
#     tujuan = fields.String()
#     isi_singkat = fields.String()
    
#     @post_load
#     def create_surat(self, data, **kwargs):
#         return models.SuratKeluar(**data)
    
# class SuratSchema(Schema):
#     id = fields.Integer()
#     isi_singkat = fields.String()
    
# class QuerySchema(Schema):
#     q = fields.String(required=False)
#     page = fields.Integer(load_default=1)
#     limit = fields.Integer(load_default=10)
    
    
# class SuratKeluarPaginationSchema(BasePaginationSchema):
#     count = fields.Integer()
#     next = fields.String(allow_none=True)
#     previous = fields.String(allow_none=True)
#     results = fields.Nested(SuratKeluarSchema, many=True)