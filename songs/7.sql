SELECT AVG(energy) FROM songs
JOIN artists ON songs.artists_id = artists.id
WHERE artists.name - 'Drake';
