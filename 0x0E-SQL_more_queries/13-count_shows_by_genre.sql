-- Lists all genres fron hbtn_0d_tvshows
-- And display the number of shows to each
SELECT name, COUNT(genre_id) AS numb
FROM tv_genres INNER JOIN
     (tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id)
     ON tv_genres.id = tv_show_genres.genre_id
GROUP BY name
ORDER BY numb DESC;
