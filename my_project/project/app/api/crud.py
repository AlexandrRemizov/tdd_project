from typing import Union
from sqlalchemy.future import select

from app.models.pydantic import SummaryPayloadSchema
from app.models.alchemy import TextSummary
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.alchemy import engine


async def post(payload: SummaryPayloadSchema) -> int:
    async with AsyncSession(bind=engine) as session:
        summary = TextSummary(url=payload.url, summary="dummy summary")
        session.add(summary)
        await session.commit()
        await session.refresh(summary)
        # обновляем объект, чтобы он был связан со сессией
    return summary.id


async def get(id: int) -> Union[dict, None]:
    async with AsyncSession(bind=engine) as session:
        query = await session.execute(
            select(TextSummary).where(TextSummary.id == id))
        result = query.scalar_one_or_none()
    return result

