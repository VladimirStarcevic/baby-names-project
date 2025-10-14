-- Pronađi 15 najpopularnijih ženskih imena (F) iz 1992. godine.
--Rezultat treba da sadrži ime, godinu i broj rođenja, sortiran po broju rođenja opadajuće.

SELECT
    name,
    year,
    count
FROM
    names
WHERE gender = 'F' AND year = 1992
ORDER BY count DESC
LIMIT 15
