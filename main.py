import json
import requests

from fastapi import FastAPI
from db import get_genres, get_tracks

app = FastAPI()

@app.get("/todos")
def list_todos():
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url)
    data = json.loads(response.text)
    return data

@app.get("/genres")
def list_genres():
    genres = get_genres()
    return genres

@app.get("/tracks")
def list_tracks():
    tracks = get_tracks()
    return tracks