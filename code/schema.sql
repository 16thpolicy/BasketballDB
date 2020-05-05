DROP TABLE IF EXISTS hall_of_fame CASCADE;
DROP TABLE IF EXISTS draft CASCADE;
DROP TABLE IF EXISTS coaches CASCADE;
DROP TABLE IF EXISTS season CASCADE;
DROP TABLE IF EXISTS master_1 CASCADE;



CREATE TABLE hall_of_fame(
    year_ numeric(4,0),
    hall_of_fame_id varchar(25),
    name varchar(127),
    category varchar(15)
);

CREATE TABLE draft(
    draft_year numeric(4,0),
    draft_round Int,
    draft_selection Int,
    draft_overall Int,
    team_id varchar(5),
    full_name varchar(127),
    --first_name varchar(25),
    --last_name varchar(25),
    suffix_name varchar(15),
    player_id varchar(25),
    draft_from_college varchar(50),
    league_id varchar(5)
);

CREATE TABLE coaches(
    coach_id varchar(30),
    year_ numeric(4,0),
    team_id varchar(5),
    league_id varchar(5),
    stint Int,
    won Int,
    lost Int,
    post_wins Int,
    post_loss Int
);


CREATE TABLE season(
    num varchar(10),
    year_ Int,
    player_name varchar(127),
    position varchar(10),
    age_ Int,
    team_id varchar(10),
    games Int,
    games_started Int,
    minute_played numeric(10,2),
    player_efficiency numeric(10,2),
    true_shooting numeric(10,2),
    three_point_attempt_percentage numeric(10,2),
    freethrow_percentage numeric(10,2),
    offensive_rebound_percentage numeric(10,2),
    defensive_rebound_percentage numeric(10,2),
    total_rebound_percentage numeric(10,2),
    assist_percentage numeric(10,2),
    steal_percentage numeric(10,2),
    block_percentage numeric(10,2),
    turnover_percentage numeric(10,2),
    usage_percentage numeric(10,2),
    blank varchar(15),
    offensive_win_share numeric(10,2),
    defensive_win_share numeric(10,2),
    win_share numeric(10,2),
    win_share_48 numeric(10,2),
    blank_2 varchar(15),
    offensive_box_plus_minus numeric(10,2),
    defensive_box_plus_minus numeric(10,2),
    box_plus_minus numeric(10,2),
    value_over_replacement numeric(10,2),
    fieldgoal numeric(10,2),
    fieldgoal_attempt numeric(10,2),
    fieldgoal_percentage numeric(10,2),
    threepoint_fg numeric(10,2),
    threepoint_fg_attempt numeric(10,2),
    threepoint_percentage numeric(10,2),
    twopoint_fg numeric(10,2),
    twopoint_fg_attempts numeric(10,2),
    twopoint_percentage numeric(10,2),
    effective_fg_percentage numeric(10,2),
    ft numeric(10,2),
    ft_attempts numeric(10,2),
    ft_percentage numeric(10,2),
    off_reb numeric(10,2),
    def_reb numeric(10,2),
    total_rebounds numeric(10,2),
    assist numeric(10,2),
    steals numeric(10,2),
    blocks numeric(10,2),
    turnovers numeric(10,2),
    points numeric(10,2),
    personal_fouls numeric(10,2),
);

CREATE TABLE master_1(
    team_id varchar(5),
    first_name varchar(30),
    last_name varchar(30),
    year_ numeric(4,0)
);



GRANT ALL PRIVILEGES ON master_1, season, draft, hall_of_fame, coaches TO postgres;

#database_final_user
