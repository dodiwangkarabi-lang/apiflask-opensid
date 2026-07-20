# from myapp.features.surat.schemas.document_schema import DocumentSchema
from myapp.features.surat import schema


class DocumentMapperService:
    _schema = schema.SuratKeluarSchema
    _schema_many = schema.SuratKeluarSchema(many=True)

    @classmethod
    def db_to_document(cls, row):
        return cls._schema.dump(row)

    @classmethod
    def db_to_documents(cls, rows):
        return cls._schema_many.dump(rows)

    @classmethod
    def document_to_db(cls, document):
        return cls._schema.load(document)

    @classmethod
    def documents_to_db(cls, documents):
        return cls._schema_many.load(documents)

# from app.models.surat_keluar import SuratKeluar
# from myapp.features.surat.models import SuratKeluar


# class DocumentMapperService:

#     @staticmethod
#     def db_to_document(row: SuratKeluar) -> dict:
#         """Mengubah satu object database menjadi document."""
#         return {
#             "id": row.id,
#             "isi_singkat": row.isi_singkat,
#             # "content": row.isi_ringkas,
#             # "metadata": {
#             #     "nomor_surat": row.nomor_surat,
#             #     "tanggal": row.tanggal_surat.isoformat() if row.tanggal_surat else None,
#             # },
#         }

#     @staticmethod
#     def db_to_documents(rows: list[SuratKeluar]) -> list[dict]:
#         """Mengubah banyak object database menjadi list document."""
#         return [
#             DocumentMapperService.db_to_document(row)
#             for row in rows
#         ]

#     @staticmethod
#     def document_to_db(document: dict) -> SuratKeluar:
#         """
#             Mengubah document menjadi object database.
            
#             Args:
#                 document (dict): Document yang akan diubah menjadi object database.
                
#                 document = {
#                     "id": "1",
#                     "title": "Surat Keluar",
#                     "isi_singkat": "Surat Keluar",
#                 }
                
#             Returns:
#                 SuratKeluar: Object database yang telah diubah.
            
#         """
        
#         row = SuratKeluar()

#         row.id = document["id"]
#         # row.perihal = document["title"]
#         row.isi_singkat = document["isi_singkat"]

#         # metadata = document.get("metadata", {})

#         # row.nomor_surat = metadata.get("nomor_surat")

#         return row

#     @staticmethod
#     def documents_to_db(documents: list[dict]) -> list[SuratKeluar]:
#         """Mengubah banyak document menjadi list object database."""
#         return [
#             DocumentMapperService.document_to_db(doc)
#             for doc in documents
#         ]