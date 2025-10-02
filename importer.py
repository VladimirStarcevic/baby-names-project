import sqlite3
import csv
import os

file_data = "data"
file_name = "example-small.csv"
file_path = os.path.join(file_data, file_name)


conn = sqlite3.connect('babynames.db')
cursor = conn.cursor()

print("Delete old data....")
cursor.execute("DELETE FROM names;")
print("Old data deleted!")

try:

    with open(file_path,encoding='UTF-8') as f_in:

        csv_reader = csv.reader(f_in)

        for row in csv_reader:
            sql_command = "INSERT INTO names (name, gender, count, year) VALUES (?, ?, ?, ?)"
            cursor.execute(sql_command, (row[0], row[1], row[2], 2023))

except FileNotFoundError:
    print(f"File  {file_name} not found")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

conn.commit()
conn.close()