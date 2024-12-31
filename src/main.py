from fastapi import FastAPI

from src.router import event_router, organizer_router

app = FastAPI()
favicon_path = 'favicon.ico'

app.include_router(event_router.router)
app.include_router(organizer_router.router)


@app.get("/")
def root():
    return {"Hola": "Pulpin 🐙"}
