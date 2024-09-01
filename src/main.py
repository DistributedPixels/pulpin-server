from fastapi import FastAPI, HTTPException
from src.controller.controlador_evento import ControladorEvento
from src.model.evento import Evento
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hola": "Pulpin 🐙"}

@app.get("/eventos", response_model=List[Evento])
async def lee_eventos():
    return await ControladorEvento.get_eventos()

@app.get("/eventos/{id_evento}", response_model=Evento)
def lee_evento(id_evento: int):
    evento = ControladorEvento.get_evento(id_evento)
    if evento is None:
        raise HTTPException(status_code=404, detail="Evento no encontrado.")
    return evento

@app.post("/eventos", response_model=Evento, status_code=201)
def crea_evento(evento: Evento):
    return ControladorEvento.crea_evento(evento)

@app.put("/eventos/{id_evento}", response_model=Evento)
def actualiza_evento(id_evento: int, evento: Evento):
    evento_actualizado = ControladorEvento.actualiza_evento(id_evento, evento)
    if evento_actualizado is None:
        raise HTTPException(status_code=404, detail="Evento no encontrado.")
    return evento_actualizado

@app.delete("/eventos/{id_evento}", status_code=204)
def elimina_event(id_evento: int):
    success = ControladorEvento.elimina_evento(id_evento)
    if not success:
        raise HTTPException(status_code=404, detail="Evento no encontrado.")