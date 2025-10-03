import sqlite3

DB_FILENAME = 'babynames.db'

def get_total_names_count() -> int:

    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()

    sql_command = "SELECT COUNT(*) FROM names;"
    cursor.execute(sql_command)

    result_tuple = cursor.fetchone()

    conn.close()

    if result_tuple:
        return result_tuple[0]
    else:
        return 0


def get_rank_for_name(year: int, name: str, gender: str) -> int:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
    sql_command = """
            SELECT rank FROM (
                SELECT 
                    name, 
                    RANK() OVER (ORDER BY count DESC) as rank
                FROM names
                WHERE year = ? AND gender = ?
            )
            WHERE name = ?
        """

    cursor.execute(sql_command, (year, gender, name))
    result_tuple = cursor.fetchone()
    conn.close()

    if result_tuple:
        return result_tuple[0]
    else:
        return -1

def get_name_by_rank(year: int, gender: str, rank: int) -> str:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
    sql_command = """
        SELECT name 
        FROM names 
        WHERE year = ? AND gender = ? 
        ORDER BY count DESC 
        LIMIT 1 OFFSET ?
    """
    offset_value = rank - 1

    parameters = (year, gender, offset_value)

    cursor.execute(sql_command, parameters)
    result = cursor.fetchone()
    conn.close()

    if result:
        return result[0]
    else:
        return "NO NAME"


def get_top_names(year: int, gender: str, limit: int = 10) -> list:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
    sql_command = """
    SELECT name
    FROM names
    WHERE year = ? AND gender = ?
    ORDER BY count DESC
    LIMIT ? 
    """

    parameters = (year, gender, limit)
    cursor.execute(sql_command, parameters)
    results_list_of_tuples = cursor.fetchall()
    conn.close()

    return [row[0] for row in results_list_of_tuples]


def get_popularity_over_time(name:str, gender: str) -> list:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
    sql_command = """
    SELECT year, count
    FROM names
    WHERE name = ? AND gender = ?
    ORDER BY year ASC
    """

    parameters = (name, gender)
    cursor.execute(sql_command, parameters)
    results_list_of_tuples = cursor.fetchall()
    conn.close()

    final_list = []
    for row_tuple in results_list_of_tuples:
        year_data_dict = {"year": row_tuple[0], "count": row_tuple[1]}
        final_list.append(year_data_dict)

    return final_list


def get_total_births_by_year(year: int) -> int:
    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
    sql_command = """
           SELECT SUM(count) 
           FROM names
           WHERE year = ? 
       """

    parameters = (year,)
    cursor.execute(sql_command, parameters)
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return  0
