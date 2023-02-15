--  a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT ts.title AS title, tsg.genre_id AS genre_id
	FROM tv_shows ts
	JOIN tv_show_genres tsg
	ON ts.id = tsg.show_id
	ORDER BY title, genre_id;
