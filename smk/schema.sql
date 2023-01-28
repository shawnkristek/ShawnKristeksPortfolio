-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS tag;
DROP TABLE IF EXISTS post_tag;

CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL,
  email TEXT NOT NULL
);

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  parent_id INTEGER NULL DEFAULT NULL,
  title VARCHAR(75) NOT NULL,
  meta_title VARCHAR(100) NULL,
  slug VARCHAR(100) UNIQUE NOT NULL, 
  summary VARCHAR(255) NULL,
  published TINYINT(1) NOT NULL DEFAULT 0, 
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  published_at TIMESTAMP NULL,
  content TEXT NOT NULL,
  img VARCHAR(75) NOT NULL DEFAULT "img/portfolio/smk-1.jpg",
  FOREIGN KEY (author_id) REFERENCES user (id)
);

--TODO convert json to sql