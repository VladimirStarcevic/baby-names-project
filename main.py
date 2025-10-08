
from fastapi import FastAPI
from analyzer import NameAnalyzer
from models import (
    NameGenderYearQuery, RankResponse,
    TopNamesQuery, TopNamesResponse,
    PopularityQuery, PopularityResponse,
    TotalCountResponse,
    YearQuery, TotalBirthsResponse,
    EquivalentNameQuery, EquivalentNameResponse
)

app = FastAPI()
analyzer = NameAnalyzer(db_path="babynames.db")

@app.get("/")
def read_root():
    return {"message": "Baby Names API is running."}

@app.post("/total-count", response_model=TotalCountResponse)
def read_total_names_count():
    count = analyzer.get_total_names_count()
    return {"total_count": count}

@app.post("/rank", response_model=RankResponse)
def read_name_rank(query: NameGenderYearQuery):
    rank = analyzer.get_rank_for_name(year=query.year, name=query.name, gender=query.gender)
    return {"rank": rank, "name": query.name, "year": query.year, "gender": query.gender}

@app.post("/top-names", response_model=TopNamesResponse)
def read_top_names(query: TopNamesQuery):
    top_names = analyzer.get_top_names(year=query.year, gender=query.gender, limit=query.limit)
    return {"year": query.year, "gender": query.gender, "limit": query.limit, "names": top_names}

@app.post("/name-popularity", response_model=PopularityResponse)
def read_popularity_over_time(query: PopularityQuery):
    popularity_list = analyzer.get_popularity_over_time(name=query.name, gender=query.gender)
    return {"data": popularity_list}

@app.post("/total-births-by-year", response_model=TotalBirthsResponse)
def read_total_births_by_year(query: YearQuery):
    total_births = analyzer.get_total_births_by_year(year=query.year)
    return {"year": query.year, "total_births": total_births}

@app.post("/equivalent-name", response_model=EquivalentNameResponse)
def read_equivalent_name(query: EquivalentNameQuery):
    message = analyzer.get_equivalent_name(query.name, query.year, query.gender, query.new_year)
    return {"message": message}