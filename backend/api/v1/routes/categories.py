from typing import Annotated
from fastapi import APIRouter, Depends
from config.load import load_config
from pydantic import BaseModel
from backend.app.dependencies import get_repo
from infrastructure.database.repo.requests import RequestsRepo

config = load_config()

router = APIRouter(
    tags=['Categories'],
    prefix=config.api_prefix.v1.categories,

)


class CategorySchema(BaseModel):
    id: int
    name: str


class CategoryCreateDTO(BaseModel):
    name: str


@router.post('/')
async def create_category(
        data: CategoryCreateDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)]
) -> CategoryCreateDTO:
    new_category = await repo.categories.add_category(name=data.name)
    return CategoryCreateDTO.model_validate(new_category, from_attributes=True)


@router.get('/')
async def get_categories(repo: Annotated[RequestsRepo, Depends(get_repo)]
                         ) -> list[CategorySchema]:
    categories = await repo.categories.get_categories()
    return categories
