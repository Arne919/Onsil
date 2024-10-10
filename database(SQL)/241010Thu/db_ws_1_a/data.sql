-- Active: 1728548597688@@127.0.0.1@3306
CREATE TABLE songs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    album TEXT NOT NULL,
    genre TEXT NOT NULL,
    duration INTEGER NOT NULL
);

INSERT INTO
    songs(id, title, artist, album, genre, duration)
VALUES
    (1, 'Song 1', 'Artist 1', 'Album 1', 'Pop', 200),
    (2, 'Song 2', 'Artist 2', 'Album 2', 'Rock', 300),
    (3, 'Song 3', 'Artist 3', 'Album 3', 'Hip Hop', 250),
    (4, 'Song 4', 'Artist 4', 'Album 4', 'Electronic', 180),
    (5, 'Song 5', 'Artist 5', 'Album 5', 'R&B', 320);

UPDATE songs
SET title = 'New Title'
WHERE id = 1;