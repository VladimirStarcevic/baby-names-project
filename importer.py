import sqlite3
import csv
import os

DB_FILENAME = 'babynames.db'
DATA_FOLDER = 'data'


def extract_year_from_filename(filename: str) -> int:
    year_str = filename[3:-4]
    return int(year_str)


print("--- Starting Data Import Process ---")
conn = sqlite3.connect(DB_FILENAME)
cursor = conn.cursor()

print("Deleting old data from 'names' table...")
cursor.execute("DELETE FROM names;")

try:
    list_of_filenames = os.listdir(DATA_FOLDER)
    print(f"Found {len(list_of_filenames)} files in '{DATA_FOLDER}'.")

    for filename in list_of_filenames:
        if filename.startswith('yob') and filename.endswith('.csv'):
            print(f"Processing file: {filename}...")
            year = extract_year_from_filename(filename)
            full_path = os.path.join(DATA_FOLDER, filename)

            with open(full_path, 'r', encoding='UTF-8') as f_in:
                csv_reader = csv.reader(f_in)
                for row in csv_reader:
                    # int(row[2]) je vazan da bi count bio broj
                    data_to_insert = (row[0], row[1], int(row[2]), year)
                    cursor.execute("INSERT INTO names (name, gender, count, year) VALUES (?, ?, ?, ?)", data_to_insert)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    conn.rollback()

finally:
    print("Committing transactions...")
    conn.commit()
    conn.close()
    print("Database connection closed.")
    print("--- Data Import Process Finished ---")