SELECT genre, count(*)
FROM songs
GROUP BY genre;

SELECT genre, count(*), duration AS 'average_duration'
FROM songs
GROUP BY genre
HAVING 
    count(*) >= 1;