-- list all genres not linked to the show Dexter 
SELECT DISTINCT name, title FROM tv_genres
INNER JOIN tv_show_genres ON genre_id
INNER JOIN tv_shows ON show_id
WHERE name NOT IN (
	SELECT name FROM tv_genres 
	INNER JOIN tv_show_genres ON genre_id
	INNER JOIN tv_shows ON show_id 
	WHERE title = 'Dexter');
