-- List all the genres of the show Dexter
SELECT tv_genres.name
FROM tv_genres LEFT JOIN (
     SELECT name
     FROM tv_shows INNER JOIN
     	  (tv_show_genres INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id)
     	  ON tv_shows.id = tv_show_genres.show_id
     WHERE title='Dexter') AS genre_dexter
     ON tv_genres.name = genre_dexter.name
WHERE genre_dexter.name IS NULL
ORDER BY tv_genres.name;
