-- Pronađi koje početno slovo imena je najpopularnije (tj. ima najveći ukupan zbir count kroz sve godine i imena).
-- Rezultat treba da prikaže to jedno slovo i ukupan zbir.
-- Napomena: Ovo je teži zadatak. Trebaće ti funkcija za izdvajanje prvog slova iz stringa.
-- U SQLite-u, to je SUBSTR(name, 1, 1).

SELECT
    SUBSTR(name, 1, 1) AS first_letter,
    SUM(count) AS total_num_of_name
FROM
    names
GROUP BY
    first_letter -- U SQLite možeš koristiti alias u GROUP BY, što je super!
ORDER BY
    total_num_of_name DESC -- Sortiraj po ukupnom broju, opadajuće
LIMIT 1; -- Uzmi samo prvi red
