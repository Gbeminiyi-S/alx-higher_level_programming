-- lists all shows from `hbtn_0d_tvshows_rate` by their rating
SELECT title, SUM(rate) AS rating FROM tv_show_ratings
INNER JOIN tv_shows ON show_id = id
GROUP BY title
ORDER BY rating DESC;
