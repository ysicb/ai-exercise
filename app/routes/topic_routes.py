from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import schemas, crud

router = APIRouter()

@router.post("/topics", response_model=schemas.TopicResponse)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    return crud.create_topic(db, topic)

@router.get("/topics")
def get_topics(db: Session = Depends(get_db)):
    return crud.get_topics(db)

@router.post("/assign/{student_id}/{topic_id}")
def assign_topic(student_id: int, topic_id: int, db: Session = Depends(get_db)):
    return {"assigned": bool(crud.assign_topic(db, student_id, topic_id))}
