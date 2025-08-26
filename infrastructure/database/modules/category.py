from .base import Base


import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]



