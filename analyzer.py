import sqlite3

class NameAnalyzer:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def get_total_names_count(self) -> int:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM names;")
        total_count = cursor.fetchone()
        conn.close()
        return total_count[0] if total_count else 0

    def get_rank_for_name(self, year: int, name: str, gender: str) -> int:
        conn = sqlite3.connect(self.db_path)
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

        parameters = (year, gender, name)

        cursor.execute(sql_command, parameters)
        result = cursor.fetchone()
        conn.close()

        return result[0] if result else -1

    def get_top_names(self, year: int, gender: str, limit: int = 10) -> list:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql_command = """
            SELECT name, count FROM names
            WHERE year = ? AND gender = ?
            ORDER BY count DESC LIMIT ?
        """
        cursor.execute(sql_command, (year, gender, limit))
        results = cursor.fetchall()
        conn.close()
        return [{"name": row[0], "count": row[1]} for row in results]

    def get_popularity_over_time(self, name: str, gender: str) -> list:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql_command = """
            SELECT year, count FROM names
            WHERE name = ? AND gender = ?
            ORDER BY year ASC
        """
        cursor.execute(sql_command, (name, gender))
        results = cursor.fetchall()
        conn.close()
        return [{"year": row[0], "count": row[1]} for row in results]

    def get_total_births_by_year(self, year: int) -> list:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        sql_command = """
            SELECT SUM(count)
            FROM names 
            WHERE year = ?;
        """
        cursor.execute(sql_command, (year,))
        result_list = cursor.fetchone()
        conn.close()
        return result_list[0]

    def get_name_by_rank(self, year: int, gender: str, rank: int) -> str:
        if rank < 1:
            return "NO NAME"

        conn = sqlite3.connect(self.db_path)
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

    def get_equivalent_name(self, name: str, year: int, gender: str, new_year: int) -> str:
        original_rank = self.get_rank_for_name(year, name, gender)

        if original_rank == -1:
            return f"The name '{name}' with gender '{gender}' was not found in year {year}."

        new_name = self.get_name_by_rank(new_year, gender, original_rank)

        if new_name == "NO NAME":
            return f"No name found in year {new_year} at rank {original_rank}."

        return f"'{name}' born in {year} would be '{new_name}' if born in {new_year} (same rank: {original_rank})."