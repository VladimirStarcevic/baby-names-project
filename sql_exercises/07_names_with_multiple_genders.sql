--  Pronađi sva imena koja su u bazi zabeležena i kao muška i kao ženska.
--  Rezultat treba da prikaže samo listu tih "unisex" imena, sortiranu abecedno.

SELECT
    name
FROM
    names
WHERE gender IN ('M', 'F')
GROUP BY name
HAVING COUNT(DISTINCT gender) = 2;