# tdd_project
Код с использованием SQLAlchemy ORM:

```
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.config import get_settings, Settings
from app.models.sqlalchemy import Base


app = FastAPI()

engine = create_async_engine(os.environ.get("DATABASE_URL"))
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base.metadata.create_all(bind=engine)


@app.middleware("http")
async def db_session_middleware(request, call_next):
    async with async_session() as session:
        async with db.SessionLocal(session) as db_session:
            request.state.db = db_session
            response = await call_next(request)
    return response


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }
```

Здесь мы создаем асинхронный движок SQLAlchemy 
и сессию в `create_async_engine()` и `sessionmaker()`,
соответственно. Затем мы создаем экземпляр `Base` на 
основе схемы SQLAlchemy, которая будет использоваться в
наших определениях моделей.

