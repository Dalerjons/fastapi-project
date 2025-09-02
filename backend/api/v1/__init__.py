from .routes.categories import router as categories_router

from fastapi import APIRouter
from config.load import load_config

config = load_config()
router = APIRouter(
    prefix=config.api_prefix.v1.prefix
)

router.include_router(categories_router)
