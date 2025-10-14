-- Izračunaj ukupan broj rođenih beba po dekadama.
-- Rezultat treba da prikaže dekadu i ukupan broj rođenja.
-- Napomena: Ovo je napredniji zadatak.
-- Trebaće ti matematička operacija da grupišeš godine u dekade, na primer (year / 10) * 10 će pretvoriti 1987 u 1980.

SELECT
    SUM(count) AS total_births,
    (year / 10) * 10 AS decades
FROM
    names
GROUP BY
    decades
ORDER BY
    decades;