from sqlalchemy.orm import Session
from . import models, schemas
from typing import List


def create_genes(db: Session, genes: List[schemas.GeneCreate]):
    for gene_data in genes:
        db_gene = models.Gene(**gene_data.dict())
        db.add(db_gene)
    db.commit()
    db.refresh(db_gene)

def create_assembly(db: Session, assembly: List[schemas.AssemblyCreate]):
        for assembly_data in assembly:
            db_assembly = models.Assembly(**assembly_data.dict())
            db.add(db_assembly)
        db.commit()
        db.refresh(db_assembly)

def create_region(db: Session, region: List[schemas.RegionCreate]):
    for region_data in region:
        db_region = models.Region(**region_data.dict())
        db.add(db_region)
    db.commit()
    db.refresh(db_region)

def create_transcript(db: Session, transcript: List[schemas.TranscriptCreate]):
    for transcript_data in transcript:
        db_transcript = models.Transcript(**transcript_data.dict())
        db.add(db_transcript)
    db.commit()
    db.refresh(db_transcript)

def create_transcript_location(db: Session, transcript_location: List[schemas.TranscriptLocationCreate]):
    for transcript_location_data in transcript_location:
        db_transcript_location = models.TranscriptLocation(**transcript_location_data.dict())
        db.add(db_transcript_location)
    db.commit()
    db.refresh(db_transcript_location)