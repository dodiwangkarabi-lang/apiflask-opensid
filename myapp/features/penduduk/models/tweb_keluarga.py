# from __future__ import annotations
# from typing import TYPE_CHECKING

# if TYPE_CHECKING:
#     from myapp.features.auth.models.config_model import Config

# from datetime import datetime

# from sqlalchemy import DateTime, ForeignKey, Integer, String, TIMESTAMP
# from sqlalchemy.orm import Mapped, mapped_column, relationship

# from myapp.extensions import db


# class TwebKeluarga(db.Model):
#     __tablename__ = "tweb_keluarga"

#     id: Mapped[int] = mapped_column(
#         primary_key=True,
#         autoincrement=True,
#     )

#     config_id: Mapped[int] = mapped_column(
#         ForeignKey("config.id"),
#         nullable=False,
#     )

#     no_kk: Mapped[str | None] = mapped_column(
#         String(16),
#     )

#     nik_kepala: Mapped[int | None] = mapped_column(
#         ForeignKey("tweb_penduduk.id"),
#     )

#     tgl_daftar: Mapped[datetime | None] = mapped_column(
#         TIMESTAMP,
#     )

#     kelas_sosial: Mapped[int | None] = mapped_column(
#         Integer,
#     )

#     tgl_cetak_kk: Mapped[datetime | None] = mapped_column(
#         DateTime,
#     )

#     alamat: Mapped[str | None] = mapped_column(
#         String(200),
#     )

#     id_cluster: Mapped[int | None] = mapped_column(
#         Integer,
#     )

#     updated_at: Mapped[datetime] = mapped_column(
#         TIMESTAMP,
#         nullable=False,
#     )

#     updated_by: Mapped[int | None] = mapped_column(
#         Integer,
#     )
    
#     config: Mapped["Config"] = relationship(
#         back_populates="tweb_keluarga",
#     )

# ----- versi aman -----
from datetime import datetime

from sqlalchemy import (
    DateTime,
    Integer,
    String,
    TIMESTAMP,
)
from sqlalchemy.orm import Mapped, mapped_column

from myapp.extensions import db


class TwebKeluarga(db.Model):
    __tablename__ = "tweb_keluarga"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    # FK -> config.id
    config_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    no_kk: Mapped[str | None] = mapped_column(
        String(16),
    )

    # FK -> tweb_penduduk.id
    nik_kepala: Mapped[int | None] = mapped_column(
        Integer,
    )

    tgl_daftar: Mapped[datetime | None] = mapped_column(
        TIMESTAMP,
    )

    kelas_sosial: Mapped[int | None] = mapped_column(
        Integer,
    )

    tgl_cetak_kk: Mapped[datetime | None] = mapped_column(
        DateTime,
    )

    alamat: Mapped[str | None] = mapped_column(
        String(200),
    )

    id_cluster: Mapped[int | None] = mapped_column(
        Integer,
    )

    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        nullable=False,
    )

    updated_by: Mapped[int | None] = mapped_column(
        Integer,
    )