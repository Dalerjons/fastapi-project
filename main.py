# main master
#  pull request
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from backend.api import router as api_router

app = FastAPI(
    title='My API',
    description=' My first API'
)

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)