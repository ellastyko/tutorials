
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    name TEXT NOT NULL
);