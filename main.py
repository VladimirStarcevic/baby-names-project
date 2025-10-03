from fastapi import FastAPI
from database import (get_total_names_count,
                      get_rank_for_name,
                      get_name_by_rank,
                      get_top_names,
                      get_popularity_over_time,
                      get_total_births_by_year)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World! The Baby Names API is running."}

@app.get("/names/total")
def read_total_names():
    total_count = get_total_names_count()
    return {"total_count": total_count}


@app.get("/names/rank")
def read_name_rank(year: int, name: str, gender: str):
    name_rank = get_rank_for_name(year=year, name=name, gender=gender)
    return {"name": name, "year": year, "gender": gender, "rank": name_rank}

@app.get("/name-by-rank")
def read_name_by_rank(year: int, gender: str, rank: int):
    name = get_name_by_rank(year=year, gender=gender, rank=rank)
    return {"year": year, "gender": gender, "rank": rank, "name": name}

@app.get("/name-top-rank")
def read_top_names(year: int, gender: str, limit:int):
    top_names = get_top_names(year=year, gender=gender, limit=limit)
    return {"year": year, "gender": gender, "limit": limit, "names": top_names}

@app.get("/name-popularity")
def read_name_popularity(name: str, gender: str):
    popularity_data = get_popularity_over_time(name=name, gender=gender)
    return {"popularity_over_time": popularity_data}

@app.get("/total-births-by-year")
def read_total_births_by_year(year: int):
    total_births = get_total_births_by_year(year=year)
    return {"year": year, "total_births": total_births}