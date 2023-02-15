-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT ts.title AS title, tvg.name AS name
	FROM tv_shows ts
	LEFT JOIN tv_show_genres tsg
	ON ts.id = tsg.show_id
	LEFT JOIN tv_genres tvg
	ON tvg.id = tsg.genre_id
	ORDER BY title, name;
