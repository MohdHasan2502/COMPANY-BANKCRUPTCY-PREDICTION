import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, ForeignKey, DateTime 
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# Data Table
class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    result = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f'{self.result}'
