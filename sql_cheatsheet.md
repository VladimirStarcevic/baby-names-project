# SQL & SQLite Cheat Sheet

A quick reference guide for essential SQL commands and SQLite syntax.

---

## Table of Contents
1. [Creating Tables](#creating-tables)
2. [Inserting Data](#inserting-data)
3. [Querying Data (SELECT)](#querying-data-select)
4. [Filtering Data (WHERE)](#filtering-data-where)
5. [Sorting and Limiting Results](#sorting-and-limiting-results)
6. [Aggregate Functions](#aggregate-functions)
7. [Updating and Deleting Data](#updating-and-deleting-data)
8. [Common SQLite Commands](#common-sqlite-commands)

---

## Creating Tables

```sql
-- Create a new table with columns and data types
CREATE TABLE names (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Auto-incrementing ID
    name TEXT NOT NULL,                     -- Name cannot be null
    year INTEGER,                           -- Year of birth
    gender TEXT,                            -- Gender (M/F)
    count INTEGER                           -- Number of occurrences
);

-- Create table only if it doesn't already exist
CREATE TABLE IF NOT EXISTS names (
    id INTEGER PRIMARY KEY,
    name TEXT,
    year INTEGER
);
```

**What it does:** Defines the structure of your database table with columns and their data types.

---

## Inserting Data

```sql
-- Insert a single row
INSERT INTO names (name, year, gender, count) 
VALUES ('Vladimir', 1995, 'M', 150);

-- Insert multiple rows at once
INSERT INTO names (name, year, gender, count) 
VALUES 
    ('Mary', 1880, 'F', 7065),
    ('Anna', 1880, 'F', 2604),
    ('Emma', 1880, 'F', 2003);

-- Insert with only some columns (others will be NULL or default)
INSERT INTO names (name, year) 
VALUES ('John', 2000);
```

**What it does:** Adds new records (rows) to your table.

---

## Querying Data (SELECT)

```sql
-- Select all columns from all rows
SELECT * FROM names;

-- Select specific columns
SELECT name, year FROM names;

-- Select with calculated column
SELECT name, year, count * 2 AS double_count FROM names;

-- Count total number of rows
SELECT COUNT(*) FROM names;

-- Count non-null values in a specific column
SELECT COUNT(name) FROM names;
```

**What it does:** Retrieves data from your table. `*` means "all columns".

---

## Filtering Data (WHERE)

```sql
-- Filter by exact match (text)
SELECT * FROM names WHERE name = 'Vladimir';

-- Filter by exact match (number)
SELECT * FROM names WHERE year = 1978;

-- Multiple conditions with AND
SELECT * FROM names WHERE name = 'Mary' AND year = 1880;

-- Multiple conditions with OR
SELECT * FROM names WHERE name = 'Mary' OR name = 'Anna';

-- Comparison operators
SELECT * FROM names WHERE count > 1000;
SELECT * FROM names WHERE year >= 1990 AND year <= 2000;
SELECT * FROM names WHERE year BETWEEN 1990 AND 2000;  -- Same as above

-- Pattern matching (names starting with 'M')
SELECT * FROM names WHERE name LIKE 'M%';

-- Pattern matching (names ending with 'a')
SELECT * FROM names WHERE name LIKE '%a';

-- Pattern matching (names containing 'ar')
SELECT * FROM names WHERE name LIKE '%ar%';

-- Check for NULL values
SELECT * FROM names WHERE gender IS NULL;
SELECT * FROM names WHERE gender IS NOT NULL;

-- Multiple possible values
SELECT * FROM names WHERE year IN (1990, 1995, 2000);
```

**What it does:** Filters rows based on conditions. Only rows matching the condition are returned.

---

## Sorting and Limiting Results

```sql
-- Limit number of results
SELECT * FROM names LIMIT 10;

-- Sort results (ascending - default)
SELECT * FROM names ORDER BY year;
SELECT * FROM names ORDER BY year ASC;  -- Same as above

-- Sort results (descending)
SELECT * FROM names ORDER BY count DESC;

-- Sort by multiple columns
SELECT * FROM names ORDER BY year DESC, count DESC;

-- Combine sorting and limiting (top 10 most popular names)
SELECT * FROM names ORDER BY count DESC LIMIT 10;

-- Skip first N results (pagination - skip first 10, get next 10)
SELECT * FROM names LIMIT 10 OFFSET 10;
```

**What it does:** Controls how many results you see and in what order.

---

## Aggregate Functions

```sql
-- Count rows
SELECT COUNT(*) FROM names;

-- Sum of values
SELECT SUM(count) FROM names;

-- Average
SELECT AVG(count) FROM names;

-- Minimum and maximum
SELECT MIN(year) FROM names;
SELECT MAX(count) FROM names;

-- Group by a column (get counts per year)
SELECT year, COUNT(*) AS name_count 
FROM names 
GROUP BY year;

-- Group by with aggregate (total births per year)
SELECT year, SUM(count) AS total_births 
FROM names 
GROUP BY year;

-- Filter groups (years with more than 1000 names)
SELECT year, COUNT(*) AS name_count 
FROM names 
GROUP BY year 
HAVING COUNT(*) > 1000;

-- Combining WHERE and HAVING (filter rows first, then groups)
SELECT year, COUNT(*) AS name_count 
FROM names 
WHERE gender = 'F'
GROUP BY year 
HAVING COUNT(*) > 500;
```

**What it does:** Performs calculations on groups of rows (counting, summing, averaging, etc.).

---

## Updating and Deleting Data

```sql
-- Update specific rows
UPDATE names 
SET count = 200 
WHERE name = 'Vladimir' AND year = 1995;

-- Update multiple columns
UPDATE names 
SET count = 200, gender = 'M' 
WHERE name = 'Vladimir';

-- Delete specific rows
DELETE FROM names 
WHERE year < 1900;

-- Delete all rows (keep table structure)
DELETE FROM names;

-- Drop entire table
DROP TABLE names;

-- Drop table only if it exists
DROP TABLE IF EXISTS names;
```

**What it does:** Modifies or removes existing data from your table.

---

## Common SQLite Commands

```sql
-- Show all tables in database
.tables

-- Show structure of a table
.schema names

-- Show current database file
.databases

-- Change output mode (for better readability)
.mode column
.headers on

-- Exit SQLite
.quit
-- or
.exit

-- Import CSV file
.mode csv
.import data.csv names

-- Export to CSV
.headers on
.mode csv
.output output.csv
SELECT * FROM names;
.output stdout  -- Return to normal output
```

**What it does:** SQLite-specific commands (start with `.`) for database management and configuration.

---

## Quick Reference Summary

| Command | Purpose | Example |
|---------|---------|---------|
| `SELECT` | Retrieve data | `SELECT * FROM names` |
| `WHERE` | Filter rows | `WHERE year = 1995` |
| `ORDER BY` | Sort results | `ORDER BY count DESC` |
| `LIMIT` | Limit results | `LIMIT 10` |
| `COUNT()` | Count rows | `SELECT COUNT(*) FROM names` |
| `INSERT` | Add data | `INSERT INTO names VALUES (...)` |
| `UPDATE` | Modify data | `UPDATE names SET count = 100` |
| `DELETE` | Remove data | `DELETE FROM names WHERE ...` |
| `GROUP BY` | Group rows | `GROUP BY year` |
| `JOIN` | Combine tables | `JOIN table2 ON ...` |

---

## Tips & Best Practices

1. **Always use WHERE with UPDATE/DELETE** to avoid changing all rows accidentally
2. **Test SELECT before DELETE** - run `SELECT *` with your WHERE clause first to see what will be deleted
3. **Use LIMIT during development** to work with small datasets for faster testing
4. **Quote column names** that are SQL keywords: `"year"`, `"order"`, `"table"`
5. **String values use single quotes**: `'Vladimir'`, not `"Vladimir"`
6. **NULL is special**: Use `IS NULL` or `IS NOT NULL`, not `= NULL`
7. **LIKE is case-insensitive** in SQLite by default

---

## Example Workflow

```sql
-- 1. Create table
CREATE TABLE names (id INTEGER PRIMARY KEY, name TEXT, year INTEGER);

-- 2. Insert data
INSERT INTO names (name, year) VALUES ('Vladimir', 1995);

-- 3. Query data
SELECT * FROM names WHERE year = 1995;

-- 4. Update data
UPDATE names SET year = 1996 WHERE name = 'Vladimir';

-- 5. Delete data
DELETE FROM names WHERE year < 1990;
```

---

*Keep this cheat sheet handy as you practice SQL. The more you use these commands, the more natural they'll become!*