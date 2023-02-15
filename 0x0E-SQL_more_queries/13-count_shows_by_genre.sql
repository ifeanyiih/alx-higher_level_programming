-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tvg.name AS genre, COUNT(tvsg.show_id) AS number_of_shows
FROM tv_genres tvg
JOIN tv_show_genres tvsg
ON tvg.id = tvsg.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;
