# models.py
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class Person(BaseModel):
    id: str
    name: str
    emoji: str
    country: str
    type: str
    desc: str
    interests: List[str]
    languages: List[str]
    age: int
    house: str
    points: int

class Event(BaseModel):
    id: str
    name: str
    time: str
    budget: float
    type: str
    category: str
    location: str
    description: str
    crew: List[str]

# Response model that returns hydrated people:
class EventOut(Event):
    crew_full: Optional[List[Person]] = None

class EventParticipant(BaseModel):
    id: str
    event_id: str
    user_id: str
    status: str            # "joined" | "interested" | "left"
    joined_at: datetime