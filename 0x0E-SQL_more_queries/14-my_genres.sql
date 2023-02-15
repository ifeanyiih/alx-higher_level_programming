-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name
FROM tv_genres tvg
JOIN tv_show_genres tvsg
ON tvg.id = tvsg.genre_id
JOIN tv_shows tvs
ON tvs.id = tvsg.show_id
WHERE tvs.title = "Dexter";
