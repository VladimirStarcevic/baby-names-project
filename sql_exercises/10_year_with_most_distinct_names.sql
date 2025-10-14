-- Pronađi godinu u kojoj je zabeležen najveći broj različitih (distinct) imena.
-- Rezultat treba da prikaže tu godinu i broj različitih imena.

SELECT
    year,
    COUNT(DISTINCT name) AS distinct_name_count
FROM
    names
GROUP BY
    year
ORDER BY
    distinct_name_count DESC -- Sortiraj po broju različitih imena, opadajuće
LIMIT 1; -- Uzmi samo prvi, najveći red