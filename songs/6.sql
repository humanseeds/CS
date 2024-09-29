SELECT name FROM songs WHERE artist_id = (SELECT id FROM artist WHERE name = 'Post Malone');
