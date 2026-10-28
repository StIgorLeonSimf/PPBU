from sqlalchemy import Column, Integer, String, Text, Boolean
from .db import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    description = Column(Text, nullable=True)
    completed = Column (Boolean, nullable=False, default=False)

