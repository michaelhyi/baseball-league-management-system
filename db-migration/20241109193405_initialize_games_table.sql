CREATE TABLE games (
    id INT PRIMARY KEY AUTO_INCREMENT,
    home_team_id INT NOT NULL,
    away_team_id INT NOT NULL,
    home_team_score INT NOT NULL,
    away_team_score INT NOT NULL,
    date DATETIME NOT NULL,
    location VARCHAR(255) NOT NULL,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX home_team_id_index ON games (home_team_id);
CREATE INDEX away_team_id_index ON games (away_team_id);

