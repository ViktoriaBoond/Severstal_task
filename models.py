from sqlalchemy import Column, Integer, Float, DateTime
from datetime import datetime
from database import Base

class MetalRoll(Base):
    """Определение столбцов таблицы: id, длина, вес, дата добавления, дата удаления из таблицы"""

    __tablename__ = 'metal_rolls'

    id = Column(Integer, primary_key=True, index=True)
    length = Column(Float, index=True, nullable=False)
    weight = Column(Float, index=True, nullable=False)
    date_added = Column(DateTime, index=True, default=datetime.utcnow)
    date_deleted = Column(DateTime, index=True, nullable=True)
