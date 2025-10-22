from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.responses import ORJSONResponse
from archive.model import *
from RATP import *
from events import *

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# Allow CORS from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/model/")
async def read_sentence(sentence: str = ''):
    emotion = "MODEL NOT WORKING"
    # emotion = predict_sentiment(sentence)
    return {"emotion": emotion}

@app.get("/time/")
async def read_bus(retour: bool = False):
    time = get_time(retour)
    return {"time": time}

@app.get("/home", response_class=HTMLResponse)
async def get_home():
    with open("home.html", "r", encoding="utf-8") as f:
        content = f.read()
    return HTMLResponse(content=content)

@app.get("/events", response_class=HTMLResponse)
async def get_home():
    date_start = "2025-07-22"
    date_end = "2025-07-22"
    events = get_events(date_start, date_end)
    store_events(events, "events.json")
    return ORJSONResponse(content=events)