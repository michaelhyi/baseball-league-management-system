ALTER TABLE batting_stats MODIFY COLUMN player_id INT NOT NULL UNIQUE;
ALTER TABLE pitching_stats MODIFY COLUMN player_id INT NOT NULL UNIQUE;