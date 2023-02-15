-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT title
FROM tv_shows tvs
JOIN tv_show_genres tvsg
JOIN tv_genres tvg
ON tvs.id = tvsg.show_id AND tvg.id = tvsg.genre_id
WHERE tvg.name = "Comedy"
ORDER BY title ASC;
