-- Lists all genres in the database by their rating
SELECT name, SUM(rate) AS rating
FROM tv_show_ratings INNER JOIN
     (tv_shows INNER JOIN
     		(tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
     		ON tv_shows.id = tv_show_genres.show_id)
	ON tv_show_ratings.show_id = tv_shows.id
GROUP BY name
ORDER BY rating DESC;
