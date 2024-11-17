CREATE TABLE batting_stats (
    id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT NOT NULL,

    at_bats INT NOT NULL,
    runs INT NOT NULL,
    hits INT NOT NULL,  
    total_bases INT NOT NULL,
    doubles INT NOT NULL,
    triples INT NOT NULL,
    home_runs INT NOT NULL,
    runs_batted_in INT NOT NULL,
    walks INT NOT NULL,
    strikeouts INT NOT NULL,
    stolen_bases INT NOT NULL,
    hit_by_pitch INT NOT NULL,
    sacrifice_flies INT NOT NULL
);

CREATE INDEX batting_stats_player_id ON batting_stats (player_id);
