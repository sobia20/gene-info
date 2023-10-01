from gene_info.schemas import GeneCreate, AssemblyCreate, RegionCreate, TranscriptCreate, TranscriptLocationCreate
from gene_info.crud import create_genes, create_assembly, create_region, create_transcript, create_transcript_location
from gene_info import models

def populate_db(db):
    populate_assembly(db)
    populate_gene(db)
    populate_region(db)
    populate_transcript(db)
    populate_transcript_location(db)


def populate_assembly(db):
    if db.query(models.Assembly).first() == None:
        assembly_info = [AssemblyCreate(accession_id='GCA_000001405.29'), AssemblyCreate(accession_id='GCA_000001405.14'), AssemblyCreate(accession_id='GCA_000001635.9')]

        create_assembly(db, assembly=assembly_info)


def populate_gene(db):
    if db.query(models.Gene).first() == None:
        genes_info = [GeneCreate(symbol='JAG1',stable_id='ENSG00000101384.12'), GeneCreate(symbol='JAG1',stable_id='ENSG00000101384.11'), GeneCreate(symbol='JAG1',stable_id='ENSG00000101384.7'),GeneCreate(symbol='JAG1',stable_id='ENSMUSG00000027276.8'), GeneCreate(symbol='ACE2',stable_id='ENSMUSG00000015405.16')]

        create_genes(db, genes=genes_info)


def populate_region(db):
    if db.query(models.Region).first() == None:
        region_info = [RegionCreate(name='20', assembly_id=1), RegionCreate(name='2', assembly_id=3), RegionCreate(name='X', assembly_id=3),  RegionCreate(name='20', assembly_id=2)]

        create_region(db, region=region_info)


def populate_transcript(db):
    if db.query(models.Transcript).first() == None:
        transcript_info = [TranscriptCreate(stable_id='ENST00000254958.10', gene_id=1), TranscriptCreate(stable_id='ENST00000254958.9', gene_id=2), TranscriptCreate(stable_id='ENST00000254958.5', gene_id=3),  TranscriptCreate(stable_id='ENST00000423891.2', gene_id=3), TranscriptCreate(stable_id='ENSMUST00000028735.8', gene_id=4), TranscriptCreate(stable_id='ENSMUST00000112271.10', gene_id=5)]

        create_transcript(db, transcript=transcript_info)


def populate_transcript_location(db):
    if db.query(models.TranscriptLocation).first() == None:
        transcript_location_info = [TranscriptLocationCreate(transcript_id=1,start=10637684, end=10673999, region_id=1), TranscriptLocationCreate(transcript_id=2,start=10637684, end=10674107, region_id=1), TranscriptLocationCreate(transcript_id=3,start=10618332, end=10654694, region_id=4),  TranscriptLocationCreate(transcript_id=4,start=10618407, end=10643154, region_id=4), TranscriptLocationCreate(transcript_id=5,start=136923376, end=136958564, region_id=2), TranscriptLocationCreate(transcript_id=6,start=162922328, end=162971416, region_id=3)]

        create_transcript_location(db, transcript_location=transcript_location_info)