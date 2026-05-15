from contextlib import asynccontextmanager
from fastapi import FastAPI
# from easy.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Тут импортируем вызываем функцию для подключение к БД
    # await init_db()
    yield