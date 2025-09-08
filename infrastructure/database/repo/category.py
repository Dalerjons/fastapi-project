from .base import BaseRepo

import sqlalchemy as sa

from infrastructure.database.modules.category import Category


class CategoryRepo(BaseRepo):
    async def add_category(self, name: str):
        query = sa.insert(Category).values(
            name=name
        ).returning(Category)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one()

    async def get_categories(self):
        query = sa.select(Category)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_category_by_id(self, category_id: int):
        query = sa.select(Category).where(Category.id == category_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def delete_category(self, category_id: int):
        query = sa.delete(Category).where(Category.id == category_id).returning(Category)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one_or_none()


    async def update_category(self, category_id: int, name: str):
        query = sa.update(Category).where(Category.id == category_id).values(name=name).returning(Category)
        result = await self.session.execute(query)
        await self.session.commit()
        return result.scalar_one_or_none()
