-- Pronađi godinu u kojoj je ime 'Michael' bilo najpopularnije,
-- kao i broj rođenja te godine. Rezultat treba da prikaže ime,
-- tu "vršnu" godinu i broj rođenja.

SELECT
    name,
    year,
    count
FROM
    names
WHERE name = 'Michael'
ORDER BY
    count DESC
LIMIT 1
