import psycopg2
import pandas as pd

connection_string = "host='localhost' dbname='database_final' user='database_final_user' password='database_final'"

# TODO add your code here (or in other files, at your discretion) to load the data


def main():
    # TODO invoke your code to load the data into the database
    print("Loading data")
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    
    data_coach = pd.read_csv(r'basketball_coaches.csv')
    data_draft = pd.read_csv(r'basketball_draft.csv')
    data_hall_of_fame = pd.read_csv(r'basketball_hof.csv')
    data_season = pd.read_csv(r'/Seasons_Stats.csv/nba-players-stats/Seasons_Stats.csv')
    
    coach = pd.DataFrame(data_coach,columns = ['coach_name','year','team_name','league_id','stint','won','lost','post_win','post_loss'])
    
    draft = pd.DataFrame(data_draft,columns = ['draft_year','draft_round','draft_selection','draft_overall','team_id','firstname','lastname','suffix','player_id','college','league_id'])
    
    hall_of_fame = pd.DataFrame(data_hall_of_fame,columns = ['year','hall_of_fame_id','name','category'])
    
    seasons = pd.DataFrame(data_season,columns = ['year','player_name','position','age','team','games','games_start','min_play','player_efficiency','true_shot','threepercent','freethrow_percent','off_reb_per','def_reb_per','all_reb_per','ass_per','steal_per','block_per','turnover_per','usage_per','fieldgoal_tot','fieldgoal_attempt','fg_per','twopoint_per','threepoint_per','tot_reb','assist','steals','blocks','points','personal_fouls'])
    
    
    for i in coach.itertuples():
        cursor.execute('''
                INSERT INTO database_final.dbo.coaches (coach_id, year_, team_id,league_id,stint,won,lost,post_wins,post_loss)
                VALUES (?,?,?,?,?,?,?,?,?)
                ''',
                i.coach_name,
                i.year,
                i.team_name,
                i.league_id,
                i.stint,
                i.won,
                i.lost,
                i.post_win,
                i.post_loss
                )

    
    
    for i in draft.itertuples():
        cursor.execute('''
                INSERT INTO database_final.dbo.draft (draft_year,draft_round,draft_selection,draft_overall,team_id,first_name,last_name,suffix_name,player_id,draft_from_college,league_id)
                VALUES (?,?,?,?,?,?,?,?,?,?,?)
                ''',
                i.draft_year,
                i.draft_round,
                i.draft_selection,
                i.draft_overall,
                i.team_id,
                i.firstname,
                i.lastname,
                i.suffix,
                i.player_id,
                i.college,
                i.league_id
                )
       
   
    
    for i in hall_of_fame.itertuples():
        cursor.execute('''
                INSERT INTO database_final.dbo.hall_of_fame (year_,hall_of_fame_id,name,category)
                VALUES (?,?,?,?)
                ''',
                i.year,
                i.hall_of_fame_id,
                i.name,
                i.category
                )
        
    
    
    for i in seasons.itertuples():
        cursor.execute('''
                INSERT INTO database_final.dbo.season (year_, player_name, position,age_ ,team_id ,games ,games_started ,minute_played ,player_efficiency ,true_shooting ,three_point_attempt_percentage ,freethrow_percentage,offensive_rebound_percentage ,defensive_rebound_percentage ,total_rebound_percentage ,assist_percentage ,steal_percentage ,block_percentage ,turnover_percentage ,usage_percentage ,fieldgoal ,fieldgoal_attempt ,fieldgoal_percentage ,twopoint_percentage ,threepoint_percentage ,total_rebounds ,assist ,steals ,blocks ,points ,personal_fouls)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                ''',
                i.year,
                i.player_name,
                i.position,
                i.age,
                i.team,
                i.games,
                i.games_start,
                i.min_play,
                i.player_efficiency,
                i.true_shot,
                i.threepercent,
                i.freethrow_percent,
                i.off_reb_per,
                i.def_reb_per,
                i.all_reb_per,
                i.ass_per,
                i.steal_per,
                i.block_per,
                i.turnover_per,
                i.usage_per,
                i.fieldgoal_tot,
                i.fieldgoal_attempt,
                i.fg_per,
                i.twopoint_per,
                i.threepoint_per,
                i.tot_reb,
                i.assist,
                i.steals,
                i.blocks,
                i.points,
                i.personal_fouls
       

   

if __name__ == "__main__":
    main()
