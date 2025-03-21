from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List


class MetalRollBase(BaseModel):
    """Базовая модель, содержит общие поля для всех моделей"""
    length: float
    weight: float


class MetalRollResponse(MetalRollBase):
    """Модель с описанием рулона, позволяет создавать экземпляры этой модели из объектов с атрибутами"""
    id: int
    date_added: datetime
    date_deleted: Optional[datetime] = None

    class Config:
        from_attributes = True


class MetalRollCreate(MetalRollBase):
    """Модель для создания рулона"""
    pass


class MetalRollDelete(MetalRollBase):
    """Модель для удаления рулона"""
    pass


class MetalRollFilter(BaseModel):
    """Модель для фильтрации рулонов по заданному диапозону объектов"""
    id: Optional[List[int]] = None
    weight_range: Optional[List[float]] = None
    length_range: Optional[List[float]] = None
    date_added_range: Optional[List[datetime]] = None
    date_deleted_range: Optional[List[datetime]] = None
