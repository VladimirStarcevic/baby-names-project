import sqlite3
import csv
import os

DB_FILENAME = 'babynames.db'
DATA_FOLDER = 'data'


def extract_year_from_filename(file_in: str) -> int:
    return int(file_in[3:-4])

conn = sqlite3.connect(DB_FILENAME)
cursor = conn.cursor()


print("Deleting old data from data base 'names'...")
cursor.execute("DELETE FROM names;")
print("Old data successfully deleted.")


try:

    list_of_filenames = os.listdir(DATA_FOLDER)
    print(f"Found {len(list_of_filenames)} files in folder '{DATA_FOLDER}'.")

    for filename in list_of_filenames:


        if filename.startswith('yob') and filename.endswith('.csv'):

            print(f"Processing file: {filename}...")

            full_path = os.path.join(DATA_FOLDER, filename)
            year = extract_year_from_filename(filename)

            with open(full_path, 'r', encoding='UTF-8') as f_in:
                csv_reader = csv.reader(f_in)


                for row in csv_reader:
                    sql_command = "INSERT INTO names (name, gender, count, year) VALUES (?, ?, ?, ?)"
                    cursor.execute(sql_command, (row[0], row[1], row[2], year))

except FileNotFoundError:
    print(f"ERROR: The folder '{DATA_FOLDER}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("Committing transactions to the database...")
conn.commit()
print("Transactions successfully saved.")

conn.close()

print("Process finished.")