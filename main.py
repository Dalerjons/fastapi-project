# main master
#  pull request

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='My API',
    description=' My first API'
)


class CategorySchema(BaseModel):
    id: int
    name: str


@app.get('/api/categories')
def get_categories() -> list[CategorySchema]:
    categories = [CategorySchema(id=i, name=f'category-{i}')for i in range(1, 11)]
    return categories
