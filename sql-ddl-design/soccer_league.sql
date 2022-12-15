-- from terminal run:
-- psql < medical_center.sql

DROP DATABASE IF EXISTS soccer_league;

CREATE DATABASE soccer_league;

\c soccer_league

CREATE TABLE teams
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL    
);

CREATE TABLE players
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    birth_date DATE NOT NULL,
    current_team_id INTEGER REFERENCES teams
);

CREATE TABLE season
(
    id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
    
);

CREATE TABLE referee
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE matches
(
    id SERIAL PRIMARY KEY,
    home_team_id INTEGER REFERENCES teams,
    away_team_id INTEGER REFERENCES teams,
    location TEXT NOT NULL,
    match_date DATE NOT NULL,
    start_time TEXT NOT NULL,
    season_id INTEGER REFERENCES season,
    head_referee_id INTEGER REFERENCES referee
    assistant_referee_1_id INTEGER REFERENCES referee,
    assistant_referee_2_id INTEGER REFERENCES referee
);

CREATE TABLE goals
(
    id SERIAL PRIMARY KEY,
    player_id INTEGER REFERENCES players NOT NULL,
    match_id INTEGER REFERENCES matches ON DELETE CASCADE
);

CREATE TABLE results
(
    id SERIAL PRIMARY KEY,
    team_id INTEGER REFERENCES teams NOT NULL,
    match_id INTEGER REFERENCES matches,
    result TEXT NOT NULL
);