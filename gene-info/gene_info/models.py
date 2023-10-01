from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Assembly(Base):
    __tablename__ = "assembly"

    id = Column(Integer, primary_key=True, autoincrement=True)
    accession_id = Column(String(50), nullable=True)


class Gene(Base):
    __tablename__ = "gene"

    gene_id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(50, collation='utf8mb4_0900_ai_ci'), nullable=False)
    stable_id = Column(String(50, collation='utf8mb4_0900_ai_ci'), nullable=False)

    transcripts = relationship('Transcript', back_populates='gene')


class Region(Base):
    __tablename__ = 'region'

    region_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50, collation='utf8mb4_0900_ai_ci'), nullable=True)
    assembly_id = Column(Integer, ForeignKey('assembly.id'))


class Transcript(Base):
    __tablename__ = 'transcript'

    transcript_id = Column(Integer, primary_key=True, autoincrement=True)
    stable_id = Column(String(50), nullable=False)
    gene_id = Column(Integer, ForeignKey('gene.gene_id'), nullable=False)

    gene = relationship('Gene', back_populates='transcripts')


class TranscriptLocation(Base):
    __tablename__ = 'transcript_location'

    id = Column(Integer, primary_key=True, autoincrement=True)
    transcript_id = Column(Integer, ForeignKey('transcript.transcript_id'), nullable=False)
    start = Column(Integer, nullable=False)
    end = Column(Integer, nullable=False)
    region_id = Column(Integer, ForeignKey('region.region_id'), nullable=False)

