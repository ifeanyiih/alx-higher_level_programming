--  a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT ts.title AS title, tsg.id AS genre_id
	FROM tv_shows ts
	JOIN tv_shows_genres tsg
	ON ts.id = tsg.show_id;
