from apiflask import Schema, fields

class KategoriResponseSchema(Schema):
    id = fields.Integer()
    config_id = fields.Integer()
    kode = fields.String()
    nama = fields.String()
    uraian = fields.String()
    enable = fields.Integer() 