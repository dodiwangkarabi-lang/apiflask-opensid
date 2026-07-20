# # auth/models.py

# from __future__ import annotations

# from typing import TYPE_CHECKING

# from datetime import datetime
# from sqlalchemy import (
#     String,
#     Integer,
#     Boolean,
#     DateTime,
#     Text,
#     ForeignKey
# )
# from sqlalchemy.orm import Mapped, mapped_column, relationship

# if TYPE_CHECKING:
#     from myapp.features.auth.models.config_model import Config

# from myapp.extensions import db

# class User(db.Model):
#     __tablename__ = "user"

#     id: Mapped[int] = mapped_column(
#         Integer,
#         primary_key=True,
#     )
    
#     config_id: Mapped[int] = mapped_column(
#         ForeignKey(
#             "config.id",
#             onupdate="CASCADE",
#             ondelete="CASCADE",
#         ),
#         nullable=False,
#     )
    
#     id_grup: Mapped[int | None] = mapped_column(
#         Integer,
#         nullable=True,
#     )

#     pamong_id: Mapped[int | None] = mapped_column(
#         Integer,
#         nullable=True,
#     )

#     username: Mapped[str | None] = mapped_column(
#         String(100),
#         nullable=True,
#     )

#     password: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     remember_token: Mapped[str | None] = mapped_column(
#         String(255),
#         nullable=True,
#     )

    

#     email: Mapped[str | None] = mapped_column(
#         String(100),
#         nullable=True,
#     )

#     last_login: Mapped[datetime | None] = mapped_column(
#         DateTime,
#         nullable=True,
#     )

#     email_verified_at: Mapped[datetime | None] = mapped_column(
#         DateTime,
#         nullable=True,
#     )

#     active: Mapped[bool] = mapped_column(
#         Boolean,
#         default=False,
#         nullable=True,
#     )

#     nama: Mapped[str | None] = mapped_column(
#         String(50),
#         nullable=True,
#     )

#     id_telegram: Mapped[str] = mapped_column(
#         String(100),
#         nullable=False,
#     )

#     token: Mapped[str | None] = mapped_column(
#         String(100),
#         nullable=True,
#     )

#     token_exp: Mapped[datetime | None] = mapped_column(
#         DateTime,
#         nullable=True,
#     )

#     telegram_verified_at: Mapped[datetime | None] = mapped_column(
#         DateTime,
#         nullable=True,
#     )

#     notif_telegram: Mapped[bool] = mapped_column(
#         Boolean,
#         default=False,
#         nullable=False,
#     )

#     company: Mapped[str | None] = mapped_column(
#         String(100),
#         nullable=True,
#     )

#     phone: Mapped[str | None] = mapped_column(
#         String(20),
#         nullable=True,
#     )

#     foto: Mapped[str | None] = mapped_column(
#         String(100),
#         default="kuser.png",
#         nullable=True,
#     )

#     session: Mapped[str] = mapped_column(
#         String(40),
#         nullable=False,
#     )

#     batasi_wilayah: Mapped[bool] = mapped_column(
#         Boolean,
#         default=False,
#         nullable=False,
#     )

#     akses_wilayah: Mapped[str | None] = mapped_column(
#         Text,
#         nullable=True,
#     )
    
#     config: Mapped["Config"] = relationship(
#         back_populates="users"
#     )

from __future__ import annotations

from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    Boolean,
    DateTime,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from myapp.extensions import db


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
    )

    # hanya simpan id referensi
    config_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    id_grup: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    pamong_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    username: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    password: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    remember_token: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    last_login: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    email_verified_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=True,
    )

    nama: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    id_telegram: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    token: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    token_exp: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    telegram_verified_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
    )

    notif_telegram: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    company: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    phone: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True,
    )

    foto: Mapped[str | None] = mapped_column(
        String(100),
        default="kuser.png",
        nullable=True,
    )

    session: Mapped[str] = mapped_column(
        String(40),
        nullable=False,
    )

    batasi_wilayah: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    akses_wilayah: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )