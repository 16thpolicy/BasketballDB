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
    draft_round BIT,
    draft_selection BIT,
    draft_overall BIT,
    team_id varchar(5),
    first_name varchar(25),
    last_name varchar(25),
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
    stint Bit,
    won smallint,
    lost smallint,
    post_wins smallint,
    post_loss smallint
);


CREATE TABLE season(
    year_ numeric(4,0),
    player_name varchar(127),
    position varchar(5),
    age_ smallint,
    team_id varchar(5),
    games Int,
    games_started Int,
    minute_played Int,
    player_efficiency Float,
    true_shooting decimal(4,4),
    three_point_attempt_percentage decimal(4,4),
    freethrow_percentage decimal(4,4),
    offensive_rebound_percentage float,
    defensive_rebound_percentage float,
    total_rebound_percentage float,
    assist_percentage float,
    steal_percentage float,
    block_percentage float,
    turnover_percentage float,
    usage_percentage float,
    fieldgoal Int,
    fieldgoal_attempt Int,
    fieldgoal_percentage float,
    twopoint_percentage float,
    threepoint_percentage float,
    total_rebounds Int,
    assist Int,
    steals Int,
    blocks Int,
    points Int,
    personal_fouls Int
);

CREATE TABLE master_1(
    team_id varchar(5),
    first_name varchar(30),
    last_name varchar(30),
    year_ numeric(4,0)
);



GRANT ALL PRIVILEGES ON master_1, season, draft, hall_of_fame, coaches TO database_final_user;
