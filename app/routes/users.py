from sqlalchemy.orm import Session
from app.database import SessionLocal
from fastapi import APIRouter, Depends
from app.models.users import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users/")
def obtener_usuarios(db: Session = Depends(get_db)):
    return db.query(User).all()
