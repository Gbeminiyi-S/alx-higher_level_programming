-- lists the number of records with the same score in the table second_table of the database
SELECT score, COUNT(*) AS number
GROUP BY score Order BY number DESC;
