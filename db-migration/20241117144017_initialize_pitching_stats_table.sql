CREATE TABLE pitching_stats (
    id INT PRIMARY KEY AUTO_INCREMENT,
    player_id INT NOT NULL,

    wins INT NOT NULL,
    losses INT NOT NULL,
    earned_runs INT NOT NULL,
    games INT NOT NULL,
    games_started INT NOT NULL,
    saves INT NOT NULL,
    innings_pitched DECIMAL(4, 1) NOT NULL,
    strikeouts INT NOT NULL,
    walks INT NOT NULL,
    hits INT NOT NULL
);

CREATE INDEX pitching_stats_player_id ON pitching_stats (player_id);
