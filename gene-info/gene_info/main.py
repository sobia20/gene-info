from fastapi import Depends, FastAPI
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


@app.get('/gene')
def get_genes_by_symbol(gene_symbol: str, db: Session = Depends(get_db)):
    query = (
        db.query(
            models.Gene.symbol.label('gene_symbol'),
            models.Gene.stable_id.label('gene_stable_id'),
            models.Transcript.stable_id.label('transcript_stable_id')
        )
        .join(models.Transcript, models.Gene.gene_id == models.Transcript.gene_id)
        .filter(models.Gene.symbol == gene_symbol)
    )

    results = query.all()

    gene_data = {
        'gene_symbol': gene_symbol,
        'genes': [
            {
                'gene_stable_id': result.gene_stable_id,
                'transcript_stable_id': result.transcript_stable_id,
            }
            for result in results
        ]
    }

    return gene_data


startup_populate_db()