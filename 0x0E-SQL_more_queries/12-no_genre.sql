--  a script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT ts.title AS title, tsg.genre_id AS genre_id
	FROM tv_shows ts
	LEFT JOIN tv_show_genres tsg
	ON ts.id = tsg.show_id
	WHERE tsg.show_id is NULL
	ORDER BY title, genre_id;
