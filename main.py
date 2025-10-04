from fastapi import FastAPI
from analyzer import NameAnalyzer


app = FastAPI()
analyzer = NameAnalyzer(db_path="babynames.db")
@app.get("/")
def read_root():
    return {"message": "Hello, World! The Baby Names API is running."}

@app.get("/names/total")
def read_total_names():
    total_count = analyzer.get_total_names_count()
    return {"total_count": total_count}

@app.get("/names/rank")
def read_name_rank(year: int, name: str, gender: str):
    name_rank = analyzer.get_rank_for_name(year=year, name=name, gender=gender)
    return {"name": name, "year": year, "gender": gender, "rank": name_rank}

@app.get("/name-by-rank")
def read_name_by_rank(year: int, gender: str, rank: int):
    name = analyzer.get_name_by_rank(year=year, gender=gender, rank=rank)
    return {"year": year, "gender": gender, "rank": rank, "name": name}

@app.get("/name-top-rank")
def read_top_names(year: int, gender: str, limit:int):
    top_names = analyzer.get_top_names(year=year, gender=gender, limit=limit)
    return {"year": year, "gender": gender, "limit": limit, "names": top_names}

@app.get("/name-popularity")
def read_name_popularity(name: str, gender: str):
    popularity_data = analyzer.get_popularity_over_time(name=name, gender=gender)
    return {"popularity_over_time": popularity_data}

@app.get("/total-births-by-year")
def read_total_births_by_year(year: int):
    total_births = analyzer.get_total_births_by_year(year=year)
    return {"year": year, "total_births": total_births}
@app.get("/equivalent-name")
def read_equivalent_name(name: str, year: int, gender: str, new_year: int):
    message = analyzer.get_equivalent_name(
        name=name,
        year=year,
        gender=gender,
        new_year=new_year
    )
    return {"result_message": message}