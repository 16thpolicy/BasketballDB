import psycopg2
import os


class Basketball():

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    def was_player(self, coach_name):
        #given coach_name return True if that coach was a player otherwise False
        return False
    
    def searchplayers(self, player):
        #given part of a player_name use LIKE to find all names containing '%player%'
        #returns a list of player names in alphabetical decending order
        if player=='0':
            return []
        return ["Player1","Player2","Player3"]

    def coach_teach_most_hof(self):
        #Which coach taught the most hall of fame players
        #returns a name or coachID
        cursor = conn.cursor()
        # has {(year,teamid): coachid}
        coach_dictionary = {}
        # has {coachid : number of hof player taught}
        coach_player_dict = {}
        # has {(year,teamid): name of hof player}
        match_team_year = {}
        
        query_data = "Select coach_id,year_,team_id From coaches"
        cursor.execute(query_data)
        record_data = cursor.fetchall()
        for i in record_data:
            coach_dictionary[(i[1],i[2])] = i[0]
            coach_player_dict[i[0]] = 0
        
        
        query_1 = "Select name,year_,team_id From hall_of_fame Where season.year_ = hall_of_fame.year_ And season.player_name = hall_of_fame.name "
        
        cursor.execute(query_1)
        record_player = cursor.fetchall()
        for i in record_player:
            match_team_year[(i[1],i[2])] = i[0]
        
        for key in match_team_year:
            for key_2 in coach_dictionary:
                if(key == key_2):
                    coach_player_dict[key_2.values()]++
        
        #gets the coach id of most taught hof players
        answer = max(coach_player_dict,key = coach_player_dict.get)
        
        query_check_coach_name = "Select player_name from season Where player_name = %s"
        
        if(cursor.execute(query_check_coach_name,(answer)) != NULL):
            return (cursor.fetchone())
        else:
            return False
    
    def seasonstat(self,player,year):
        #given year and player
        #return season detail of that player
        #if player did not have stats that year return [False] otherwise return an array of stats
        query = "Select * From season Where player_name = %s and year_ = %s Order By ASC"
        cursor = conn.cursor()
        if(cursor.execute(query,(player,year)) != NULL):
            return(cursor.fetchone())
        else:
            return False
    
    def player_draft(self,player):
        #given player name return draft college and year
        cursor = self.conn.cursor();
        p=player.replace("'","\\'")
        query = "SELECT draft_year, draft_from_college FROM draft WHERE full_name = '%s'"
        cursor.execute(query%(p))
        draft_info = cursor.fetchall()
        return draft_info
    
    def teamsplayed(self,player):
        #given a playername return list of teams alphabetical order desc of all teams they were in
        cursor = self.conn.cursor();
        p=player.replace("'","\\'")
        query = "SELECT DISTINCT team_id AS Team FROM season WHERE Season.player_name = '%s' ORDER BY Team DESC"
        cursor.execute(query%(p))
        teams_played = cursor.fetchall()
        return teams_played
    
    def find_overall_per(self,player):
        #given player name return overall per
        cursor = self.conn.cursor();
        p=player.replace("'","\\'")
        query = "SELECT AVG(season.player_efficiency) FROM season WHERE season.player_name = '%s'"
        cursor.execute(query%(p))
        overall_per = cursor.fetchall()
        return overall_per
        
    def coach_team_improve(self,coach,team):
        #if the coach taught this team, take player stats from 1 season before and the season the coach was introduced
            #calculate average PER of the present players in both seasons
            #return average PER increase or decrease of the team
        #else return False
        return False
    
    def hof(self, name):
        #return year when they were inducted into HOF
        #else return False
        return False