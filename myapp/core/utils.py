# utils/exceptions.py

from apiflask import abort

def validation_error(errors):
    abort(
        400,
        message="Validation Error",
        detail=errors
    )

def not_found(message="Data tidak ditemukan"):
    abort(404, message=message)

def forbidden(message="Akses ditolak"):
    abort(403, message=message)