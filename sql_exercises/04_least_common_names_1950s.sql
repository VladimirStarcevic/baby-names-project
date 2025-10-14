-- Pronađi sva imena koja su u dekadi 1950-ih (od 1950. do 1959. godine) imala ukupan broj rođenja manji od 15.
-- Rezultat treba da prikaže ime i ukupan broj rođenja za taj period.

SELECT
    name,
    SUM(count) AS total_births
FROM
    names
WHERE year BETWEEN 1950 AND 1959
GROUP BY name
HAVING total_births < 15