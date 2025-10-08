from pydantic import BaseModel, Field
from typing import List, Literal

class NameGenderYearQuery(BaseModel):
    name: str
    year: int = Field(..., gt=1879, lt=2015)
    gender: Literal['M', 'F']
class RankResponse(BaseModel):
    rank: int
    name: str
    year: int
    gender: str

class TopNamesQuery(BaseModel):
    year: int = Field(..., gt=1879, lt=2015)
    gender: Literal['M', 'F']
    limit: int = Field(10, gt=0, le=100)
class TopNamesResponse(BaseModel):
    year: int
    gender: str
    limit: int
    names: List[dict]

class PopularityQuery(BaseModel):
    name: str
    gender: Literal['M', 'F']
class PopularityDataPoint(BaseModel):
    year: int
    count: int

class PopularityResponse(BaseModel):
    data: List[PopularityDataPoint]
class TotalCountResponse(BaseModel):
    total_count: int

class YearQuery(BaseModel):
    year: int = Field(..., gt=1879, lt=2015)
class TotalBirthsResponse(BaseModel):
    year: int
    total_births: int

class EquivalentNameQuery(BaseModel):
    name: str
    year: int = Field(..., gt=1879, lt=2015)
    gender: Literal['M', 'F']
    new_year: int = Field(..., gt=1879, lt=2015)
class EquivalentNameResponse(BaseModel):
    message: str