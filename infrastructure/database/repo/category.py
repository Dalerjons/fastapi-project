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
        pass

    async def delete_category(self):
        pass

    async def update_category(self):
        pass