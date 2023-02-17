-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name, count(tv_genres.name) FROM tv_genres
	INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.show_id
	GROUP BY tv_genres.name
	ORDER BY count(tv_genres.name) DESC;
