from .base import BaseRepo


import sqlalchemy as sa


class CategoryRepo(BaseRepo):
    async def add_category(self):
        pass

    async def get_categories(self):
        pass


    async def get_category_by_id(self, category_id: int):
        pass

    async def delete_category(self):
        pass

    async def update_category(self):
        pass