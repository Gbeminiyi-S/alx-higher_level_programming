-- list all genres not linked to the show Dexter 
SELECT DISTINCT name FROM tv_genres AS g
INNER JOIN tv_show_genres AS tg ON tg.genre_id = g.id 
INNER JOIN tv_shows AS s ON s.id = tg.show_id
WHERE g.name NOT IN (
	SELECT DISTINCT name FROM tv_genres AS g
	INNER JOIN tv_show_genres AS tg ON tg.genre_id = g.id
	INNER JOIN tv_shows AS s ON s.id = tg.show_id
	WHERE title = 'Dexter')
ORDER BY name;
