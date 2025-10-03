from fastapi import FastAPI
from database import get_total_names_count, get_rank_for_name, get_name_by_rank

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