from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    number: str

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: int
    topics: List[str] = []

    class Config:
        from_attributes = True

class TopicBase(BaseModel):
    name: str

class TopicCreate(TopicBase):
    pass

class TopicResponse(TopicBase):
    id: int
    class Config:
        from_attributes = True


class ImageSummaryResponse(BaseModel):
    summary: str
    number_of_words: int

