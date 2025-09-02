from fastapi import APIRouter
from .v1 import router as v1_router
from config.load import load_config


config = load_config()

router = APIRouter(
    prefix=config.api_prefix.prefix
)
router.include_router(v1_router)



