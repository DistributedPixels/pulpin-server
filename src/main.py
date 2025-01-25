from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.router import event_router, organizer_router

app = FastAPI()
favicon_path = 'favicon.ico'

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(event_router.router)
app.include_router(organizer_router.router)


@app.get("/")
def root():
    return {"Hola": "Pulpin 🐙"}
