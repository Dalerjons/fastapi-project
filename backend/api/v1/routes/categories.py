from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
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


@router.get('/{category_id}', response_model=CategoryCreateDTO)
async def get_category_by_id(
        category_id: int,
        repo: Annotated[RequestsRepo, Depends(get_repo)]

):
    category = await repo.categories.get_category_by_id(category_id=category_id)
    if category is None:
        raise HTTPException(status_code=404, detail=f'Category with {category_id} not found')
    return CategoryCreateDTO.model_validate(category, from_attributes=True)


@router.put('/{category_id}', response_model=CategoryCreateDTO)
async def update_category(
        category_id: int,
        data: CategoryCreateDTO,
        repo: Annotated[RequestsRepo, Depends(get_repo)]

):
    updated_category = await repo.categories.update_category(category_id, data.name)
    if updated_category is None:
        raise HTTPException(status_code=404, detail=f'Category with {category_id} not found')
    return CategoryCreateDTO.model_validate(updated_category, from_attributes=True)

