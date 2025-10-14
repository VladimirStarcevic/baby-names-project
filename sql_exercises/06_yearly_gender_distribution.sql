-- Za svaku godinu, izračunaj ukupan broj rođenih dečaka (M) i devojčica (F).
-- Rezultat treba da sadrži tri kolone: godinu, pol i ukupan broj rođenja za tu kombinaciju.
-- Sortiraj rezultat prvo po godini, a zatim po polu.

SELECT
    year,
    gender,
    SUM(count) AS total_births
FROM
    names
GROUP BY
    year, gender
ORDER BY
    year, gender;