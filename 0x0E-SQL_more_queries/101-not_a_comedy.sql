-- lists all shows without the genre `Comedy` in the database `hbtn_0d_tvshows`
SELECT DISTINCT title FROM tv_genres AS g
RIGHT JOIN tv_show_genres AS tg ON tg.genre_id = g.id 
RIGHT JOIN tv_shows AS s ON s.id = tg.show_id
WHERE title NOT IN (
		SELECT title FROM tv_genres AS g
		INNER JOIN tv_show_genres AS tg ON tg.genre_id = g.id
		INNER JOIN tv_shows AS s ON s.id = tg.show_id
		WHERE name = 'Comedy')
ORDER BY title;
