-- Active: 1728732291620@@127.0.0.1@3306
SELECT * 
FROM artists;

SELECT COUNT(*) 
FROM artists;

SELECT * 
FROM artists 
WHERE Name = 'AC/DC';

SELECT ArtistId, Name 
FROM artists;

SELECT * 
FROM artists 
WHERE Name = 'Gilberto Gil' OR Name = 'Ed Motta';

SELECT * 
FROM artists 
ORDER BY Name DESC;

SELECT * 
FROM artists 
WHERE Name LIKE 'Vinícius%' 
LIMIT 2;


SELECT ArtistId 
FROM artists 
LIMIT 21 OFFSET 49;