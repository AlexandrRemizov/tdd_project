from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TextSummary(Base):
    __tablename__ = 'text_summary'

    id = Column(Integer, primary_key=True)
    url = Column(Text)
    summary = Column(Text)
    created_at = Column(DateTime, nullable=False, default=datetime.now())

    def __str__(self):
        return self.url
