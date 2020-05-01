import psycopg2
import csv

connection_string = "host='localhost' dbname='database_final' user='database_final_user' password='database_final'"

# TODO add your code here (or in other files, at your discretion) to load the data


def main():
    # TODO invoke your code to load the data into the database
    print("Loading data")
    
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    with open('basketball_coaches.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO coaches VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s)",j)
    i.close()
    conn.commit()
    
    with open('basketball_draft.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO draft VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s,%s,%s)",j)
    i.close()
    conn.commit()
    
    with open('basketball_hof.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO hall_of_fame VALUES (%s, %s, %s, %s)",j)
    i.close()
    conn.commit()
    
    with open('Seasons_Stats.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO season VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",j)
    i.close()
    conn.commit()
    
    data_coach = pd.read_csv(r'basketball_coaches.csv')
    data_draft = pd.read_csv(r'basketball_draft.csv')
    data_hall_of_fame = pd.read_csv(r'basketball_hof.csv')
    data_season = pd.read_csv(r'Seasons_Stats.csv')
    
    coach = pd.DataFrame(data_coach,columns = ['coachID','year','tmID','lgID','stint','won','lost','post_wins','post_losses'])
    
    draft = pd.DataFrame(data_draft,columns = ['draftYear','draftRound','draftSelection','draftOverall','tmID','firstName','lastName','suffixName','playerID','draftFrom','lgID'])
    
    hall_of_fame = pd.DataFrame(data_hall_of_fame,columns = ['year','hofID','name','category'])
    
    seasons = pd.DataFrame(data_season,columns = ['Year','Player','Pos','Age','Tm','G','GS','MP','PER','TS%','3PAr','FTr','ORB%','DRB%','TRB%','AST%','STL%','BLK%','TOV%','USG%','blanl','OWS','DWS','WS','WS/48','blank2','OBPM','DBPM','BPM','VORP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS'])

    for i in coach.itertuples():
        query = "INSERT INTO coaches(coach_id, year_, team_id,league_id,stint,won,lost,post_wins,post_loss) VALUES('%s',%s,'%s','%s',%d,%d,%d,%d,%d)"%(i.coachID,i.year,i.tmID, i.lgID, i.stint, i.won, i.lost, i.post_wins, i.post_losses)
        print(query)
        cursor.execute(query)   

    for i in draft.itertuples():
        query = "INSERT INTO database_final.dbo.draft (draft_year,draft_round,draft_selection,draft_overall,team_id,first_name,last_name,suffix_name,player_id,draft_from_college,league_id)\
                VALUES (%d,%d,%d,%d,%s,%s,%s,%s,%s,%s,%s)"%(i.draftYear, i.draftRound, i.draftSelection, i.draftOverall, i.tmID, i.firstName, i.lastName, i.suffixName, i.playerID, i.draftFrom, i.lgID)
        print(query)
        cursor.execute()
       
   
    
    # for i in hall_of_fame.itertuples():
    #     cursor.execute('''
    #             INSERT INTO database_final.dbo.hall_of_fame (year_,hall_of_fame_id,name,category)
    #             VALUES (?,?,?,?)
    #             ''',
    #             i.year,
    #             i.hall_of_fame_id,
    #             i.name,
    #             i.category
    #             )
        
    
    
    # for i in seasons.itertuples():
    #     cursor.execute('''
    #             INSERT INTO database_final.dbo.season (year_, player_name, position,age_ ,team_id ,games ,games_started ,minute_played ,player_efficiency ,true_shooting ,three_point_attempt_percentage ,freethrow_percentage,offensive_rebound_percentage ,defensive_rebound_percentage ,total_rebound_percentage ,assist_percentage ,steal_percentage ,block_percentage ,turnover_percentage ,usage_percentage ,fieldgoal ,fieldgoal_attempt ,fieldgoal_percentage ,twopoint_percentage ,threepoint_percentage ,total_rebounds ,assist ,steals ,blocks ,points ,personal_fouls)
    #             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    #             ''',
    #             i.year,
    #             i.player_name,
    #             i.position,
    #             i.age,
    #             i.team,
    #             i.games,
    #             i.games_start,
    #             i.min_play,
    #             i.player_efficiency,
    #             i.true_shot,
    #             i.threepercent,
    #             i.freethrow_percent,
    #             i.off_reb_per,
    #             i.def_reb_per,
    #             i.all_reb_per,
    #             i.ass_per,
    #             i.steal_per,
    #             i.block_per,
    #             i.turnover_per,
    #             i.usage_per,
    #             i.fieldgoal_tot,
    #             i.fieldgoal_attempt,
    #             i.fg_per,
    #             i.twopoint_per,
    #             i.threepoint_per,
    #             i.tot_reb,
    #             i.assist,
    #             i.steals,
    #             i.blocks,
    #             i.points,
    #             i.personal_fouls
    #     )
       

   

    conn.close()
if __name__ == "__main__":
    main()
