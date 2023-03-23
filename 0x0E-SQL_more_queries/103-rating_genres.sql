-- lists all shows from `hbtn_0d_tvshows_rate` by their rating
SELECT name, SUM(rate) AS rating FROM tv_genres AS tg
INNER JOIN tv_show_genres AS sg ON tg.id = sg.genre_id
INNER JOIN tv_show_ratings AS tr ON sg.show_id = tr.show_id
GROUP BY name
ORDER BY rating DESC;
