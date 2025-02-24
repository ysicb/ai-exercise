from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

student_topic_association = Table(
    "student_topic",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id")),
    Column("topic_id", Integer, ForeignKey("topics.id")),
)

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    number = Column(String, unique=True, nullable=False)

    topics = relationship("Topic", secondary=student_topic_association, back_populates="students")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    students = relationship("Student", secondary=student_topic_association, back_populates="topics")
