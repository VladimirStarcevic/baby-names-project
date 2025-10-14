-- Prikaži sva muška imena (M) koja počinju slovom 'J' i završavaju se slovom 'n'.
-- Rezultat treba da sadrži samo jedinstvena imena, sortirana abecedno.

SELECT
    DISTINCT name
FROM
    names
WHERE name LIKE 'J%n'
ORDER  BY name
