from fastapi import FastAPI
from sqlalchemy.orm import Session
from gene_info import models
from gene_info.database import SessionLocal, engine
from gene_info.populate_db import populate_db

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def startup_populate_db():
    db = SessionLocal()
    try:
        populate_db(db)
    finally:
        db.close()

startup_populate_db()