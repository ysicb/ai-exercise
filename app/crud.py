from sqlalchemy.orm import Session
from app import models, schemas
from app.redis_client import redis_client
from app.config import STORAGE_BACKEND
import json

def create_student(db: Session, student: schemas.StudentCreate):
    if STORAGE_BACKEND == "redis":
        student_id = student.number  # Use `number` as a unique identifier
        student_data = {"id": student_id, "name": student.name, "number": student.number}
        redis_client.hset(f"student:{student_id}", mapping=student_data)
        return student_data  # Now includes `id`
    else:
        db_student = models.Student(name=student.name, number=student.number)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

def get_students(db: Session):
    if STORAGE_BACKEND == "redis":
        keys = redis_client.scan_iter("student:*")
        students = [redis_client.hgetall(key) for key in keys]
        return students
    else:
        return db.query(models.Student).all()

def delete_student(db: Session, student_id: int):
    if STORAGE_BACKEND == "redis":
        if redis_client.exists(f"student:{student_id}"):
            redis_client.delete(f"student:{student_id}")
            return True
        return False
    else:
        student = db.query(models.Student).filter(models.Student.id == student_id).first()
        if student:
            db.delete(student)
            db.commit()
            return True
        return False

def create_topic(db: Session, topic: schemas.TopicCreate):
    if STORAGE_BACKEND == "redis":
        topic_id = redis_client.incr("topic:id_counter")  # Auto-incrementing ID
        topic_data = {"id": topic_id, "name": topic.name}
        redis_client.hset(f"topic:{topic_id}", mapping=topic_data)
        return topic_data  # Now includes "id"
    else:
        db_topic = models.Topic(name=topic.name)
        db.add(db_topic)
        db.commit()
        db.refresh(db_topic)
        return db_topic

def get_topics(db: Session):
    if STORAGE_BACKEND == "redis":
        keys = redis_client.scan_iter("topic:*")  # Use scan_iter for better performance
        topics = [redis_client.hgetall(key) for key in keys]
        return [{"id": key.split(":")[1], **topic} for key, topic in zip(keys, topics)]
    else:
        return db.query(models.Topic).all()


def assign_topic(db: Session, student_id: int, topic_id: int):
    if STORAGE_BACKEND == "redis":
        redis_client.sadd(f"student:{student_id}:topics", str(topic_id))  # Store as string
        return True
    else:
        student = db.query(models.Student).filter(models.Student.id == student_id).first()
        topic = db.query(models.Topic).filter(models.Topic.id == topic_id).first()
        if student and topic:
            student.topics.append(topic)
            db.commit()
            return student
        return None

