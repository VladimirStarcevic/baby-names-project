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
