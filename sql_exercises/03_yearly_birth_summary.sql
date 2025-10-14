-- Za svaku godinu od 2000. do 2010. (uključujući obe), izračunaj ukupan broj rođenih beba.
-- Rezultat treba da sadrži godinu i ukupan broj rođenja, sortiran hronološki.

SELECT
    year,
    SUM(count) AS total_num_of_births
FROM
    names
WHERE year BETWEEN 2000 AND 2010
GROUP BY year
ORDER BY year