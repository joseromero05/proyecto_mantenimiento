from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import models, schemas
from database import engine, Base, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    solicitudes = db.query(models.Request).all()
    return templates.TemplateResponse("index.html", {"request": request, "solicitudes": solicitudes})

@app.post("/solicitud")
def crear_solicitud(
    user_id: int = Form(...),
    equipment_id: int = Form(...),
    tipo: str = Form(...),
    descripcion: str = Form(...),
    db: Session = Depends(get_db)
):
    nueva = models.Request(user_id=user_id, equipment_id=equipment_id, type=tipo, description=descripcion)
    db.add(nueva)
    db.commit()
    return RedirectResponse("/", status_code=303)
