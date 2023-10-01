from pydantic import BaseModel


class AssemblyBase(BaseModel):
    accession_id: str

class AssemblyCreate(AssemblyBase):
    pass

class Assembly(AssemblyBase):
    id: int

    class COnfig:
        orm_mode = True


class GeneBase(BaseModel):
    symbol: str
    stable_id: str

class GeneCreate(GeneBase):
    pass

class Gene(GeneBase):
    gene_id: int

    class Config:
        orm_mode = True


class RegionBase(BaseModel):
    name: str
    assembly_id: int

class RegionCreate(RegionBase):
    pass

class Region(RegionBase):
    region_id: int

    class Config:
        orm_mode = True


class TranscriptBase(BaseModel):
    stable_id: str
    gene_id: int

class TranscriptCreate(TranscriptBase):
    pass

class Transcript(TranscriptBase):
    transcript_id: int

    class Config:
        orm_mode = True


class TranscriptLocationBase(BaseModel):
    transcript_id: int
    start: int
    end: int
    region_id: int

class TranscriptLocationCreate(TranscriptLocationBase):
    pass

class TranscriptLocation(TranscriptLocationBase):
    id: int

    class Config:
        orm_mode = True