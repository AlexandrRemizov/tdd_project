import os
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .config import get_settings, Settings
from .models.alchemy import Base

app = FastAPI()

engine = create_async_engine(os.environ.get("DATABASE_URL"))
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)


@app.get("/ping")
def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
