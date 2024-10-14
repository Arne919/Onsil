-- Active: 1728547258120@@127.0.0.1@3306
SELECT * 
FROM tracks
WHERE Name LIKE '%love%';

SELECT *
FROM tracks
WHERE 
    GenreId = 1
    AND Milliseconds >= 300000
ORDER BY unitPrice DESC;

SELECT GenreId, COUNT(*) AS TotalTracks
FROM tracks
GROUP BY GenreId;

SELECT GenreId, COUNT(*) AS TotalTracks
FROM tracks
GROUP BY 
    GenreId
HAVING 
    COUNT(*) >= 100;