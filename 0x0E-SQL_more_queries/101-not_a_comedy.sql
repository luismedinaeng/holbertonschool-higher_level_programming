-- Lists all genres from hbtn_0d_tvshows
-- that has a Comedy genre
SELECT tv_shows.title
FROM tv_shows LEFT JOIN (
     SELECT title
     FROM tv_genres INNER JOIN
     	  (tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id)
     	  ON tv_genres.id = tv_show_genres.genre_id
     WHERE name = 'Comedy') AS title_comedy
     ON tv_shows.title = title_comedy.title
WHERE title_comedy.title IS NULL
ORDER BY title;
