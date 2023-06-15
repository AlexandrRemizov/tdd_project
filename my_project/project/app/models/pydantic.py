from pydantic import BaseModel
from datetime import datetime


class SummaryPayloadSchema(BaseModel):
    url: str


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummarySchema(SummaryResponseSchema):
    class Config:
        orm_mode = True
    summary: str
    created_at: datetime
