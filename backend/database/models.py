from sqlalchemy import JSON, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from backend.database.connection import Base

class Agent(Base):
    __tablename__="agents"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    description=Column(String)
    config=Column(JSON,nullable=False)
    created_at=Column(
        DateTime,
        server_default=func.now()
    )
    updated_at=Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )