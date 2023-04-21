import os
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from .models.alchemy import Base
from .models.alchemy import engine
from .config import get_settings, Settings
from .models.alchemy import Base
from app.api import ping


def create_application() -> FastAPI:
    application = FastAPI()

    application.include_router(ping.router)

    return application


app = create_application()
