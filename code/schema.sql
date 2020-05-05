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
    won varchar(5),
    lost varchar(5),
    post_wins varchar(5) ,
    post_loss varchar(5)
);


CREATE TABLE season(
    num varchar(10),
    year_ Int,
    player_name varchar(127),
    position varchar(10),
    age_ varchar(10),
    team_id varchar(10),
    games varchar(10),
    games_started varchar(10),
    minute_played varchar(10),
    player_efficiency NUMERIC(4,2),
    true_shooting varchar(15),
    three_point_attempt_percentage varchar(15),
    freethrow_percentage varchar(15),
    offensive_rebound_percentage varchar(15),
    defensive_rebound_percentage varchar(15),
    total_rebound_percentage varchar(10),
    assist_percentage varchar(10),
    steal_percentage varchar(10),
    block_percentage varchar(10),
    turnover_percentage varchar(10),
    usage_percentage varchar(15),
    blank varchar(15),
    offensive_win_share varchar(15),
    defensive_win_share varchar(15),
    win_share varchar(15),
    win_share_48 varchar(15),
    blank_2 varchar(15),
    offensive_box_plus_minus varchar(15),
    defensive_box_plus_minus varchar(15),
    box_plus_minus varchar(15),
    value_over_replacement varchar(15),
    fieldgoal varchar(10),
    fieldgoal_attempt varchar(10),
    fieldgoal_percentage varchar(10),
    threepoint_fg varchar(10),
    threepoint_fg_attempt varchar(10),
    threepoint_percentage varchar(15),
    twopoint_fg varchar(10),
    twopoint_fg_attempts varchar(10),
    twopoint_percentage varchar(10),
    effective_fg_percentage varchar(10),
    ft varchar(10),
    ft_attempts varchar(10),
    ft_percentage varchar(10),
    off_reb varchar(10),
    def_reb varchar(10),
    total_rebounds varchar(10),
    assist varchar(10),
    steals varchar(10),
    blocks varchar(10),
    turnovers varchar(10),
    personal_fouls varchar(10),
    points Int
);

CREATE TABLE master_1(
    team_id varchar(5),
    first_name varchar(30),
    last_name varchar(30),
    year_ numeric(4,0)
);



GRANT ALL PRIVILEGES ON master_1, season, draft, hall_of_fame, coaches TO database_final_user;




