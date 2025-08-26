from dataclasses import dataclass

from .category import CategoryRepo
from sqlalchemy.ext.asyncio import AsyncSession

@dataclass
class RequestsRepo:
    session: AsyncSession


    @property
    def categories(self) -> CategoryRepo:
        return CategoryRepo(self.session)