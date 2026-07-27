from sqlalchemy import Integer, String, Text
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy.orm import Mapped, mapped_column

from myapp.extensions import db

class KlasifikasiSurat(db.Model):
    __tablename__ = "klasifikasi_surat"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    config_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
        index=True,
    )

    kode: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    nama: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    uraian: Mapped[str] = mapped_column(
        MEDIUMTEXT,
        nullable=False,
    )

    enabled: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
        server_default="1",
    )