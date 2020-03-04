-- Lists all genres fron hbtn_0d_tvshows
-- And display the number of shows to each
SELECT name as genre, COUNT(show_id) AS number_of_shows
FROM tv_genres INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
