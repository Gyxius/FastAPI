# main.py
from fastapi import FastAPI, Query
from typing import List
from db_fake import people, events
from models import EventOut, Person
from auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)

@app.get("/people")
def get_people():
    return people


# quick index for people by id
people_by_id = {p.id: p for p in people}

@app.get("/events", response_model=List[EventOut])
def list_events(expand: bool = Query(False)):
    people_by_id = {p.id: p for p in people}

    result: List[EventOut] = []
    for e in events:
        base = e.model_dump()  # Pydantic v2
        crew_full = [people_by_id[pid] for pid in e.crew if pid in people_by_id] if expand else None

        # EventOut extends Event and adds crew_full
        result.append(EventOut(**base, crew_full=crew_full))

    return result

# Return the events that the user joined
@app.get("/userevents", response_model=List)
def list_user_events(user_id: str = Query("u1")):
    result: List = []
    for e in events:
        if user_id in e.crew:
            result.append(e)

    return result

