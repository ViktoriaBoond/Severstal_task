from fastapi import FastAPI, Depends, HTTPException, Query
import uvicorn
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
import database
from models import Base, MetalRoll
from schemas import MetalRollCreate, MetalRollResponse, MetalRollFilter, MetalRollDelete


app = FastAPI()    # Создание экземпляра приложения

Base.metadata.create_all(bind=database.engine)    # Создание базы данных


if __name__ == '__main__':    # Автоматическая перезагрузка при внесении изменений
    uvicorn.run('main:app', reload=True)


def get_db():    # Зависимость для получения сессии базы данных
    db = database.session_local()
    try:
        yield db
    finally:
        db.close()


@app.post('/rolls/', response_model=MetalRollResponse)
async def create_roll(metalroll: MetalRollCreate, db: Session = Depends(get_db)) -> MetalRoll:
    db_roll = MetalRoll(length=metalroll.length, weight=metalroll.weight)
    db.add(db_roll)
    db.commit()
    db.refresh(db_roll)

    return db_roll


@app.delete('/rolls/{roll_id}', response_model=MetalRollDelete)
async def delete_roll(roll_id: int, db: Session = Depends(get_db)) -> MetalRoll:
    db_roll = db.query(MetalRoll).filter(MetalRoll.id == roll_id).first()
    if db_roll is None:
        raise HTTPException(status_code=404, detail="Roll not found")
    db.delete(db_roll)
    db.commit()

    return db_roll


@app.get('/rolls/', response_model=List[MetalRollFilter])
async def get_rolls(
        db: Session = Depends(get_db),
        id: Optional[int] = Query(None),
        weight: Optional[float] = Query(None),
        length: Optional[float] = Query(None),
        added_date: Optional[date] = Query(None),
        removed_date: Optional[date] = Query(None)
) -> List[MetalRoll]:
    query = db.query(MetalRoll)

    if id is not None:
        query = query.filter(MetalRoll.id == id)
    if weight is not None:
        query = query.filter(MetalRoll.weight == weight)
    if length is not None:
        query = query.filter(MetalRoll.length == length)
    if added_date is not None:
        query = query.filter(MetalRoll.added_date == added_date)
    if removed_date is not None:
        query = query.filter(MetalRoll.removed_date == removed_date)

    return query.all()



