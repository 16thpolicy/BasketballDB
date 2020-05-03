import psycopg2
import os


class Basketball():

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    def was_player(self, coach_name):
        #given coach_name return True if that coach was a player otherwise False
        coach = coach_name.lower()
        query = "Select player_name From season Where LOWER(player_name) = %s"
        cursor = self.conn.cursor()
        cursor.execute(query%(coach))
        first_row = cursor.fetchone()
        if len(first_row) != 0:
            return True
        else:
            return False
    
    def searchplayers(self, player):
        #given part of a player_name use LIKE to find all names containing '%player%'
        #returns a list of player names in alphabetical decending order
        p = player.lower()
        p = player.replace("'","\\'")
        
        query = "Select DISTINCT player_name From season Where player_name LIKE '%%%s%%' ORDER BY player_name DESC"
        cursor = self.conn.cursor()
        cursor.execute(query%(p))
        player_names = cursor.fetchall()
        if len(player_names) != 0:
            player_list = []
            for i in player_names:
                player_list.append(i)
            return player_list
            
        return []
    

    
    def coach_teach_most_hof_year(self,year1,year2):
        #Which coach taught the most hall of fame players
        #returns a name or coachID
        cursor = self.conn.cursor()
        year1 = year1.replace("'","\\'")
        year2 = year2.replace("'","\\'")
        # has {(year,teamid): coachid}
        coach_dictionary = {}
        
        # has {(year,teamid): name of hof player}
        match_team_year = {}
        
        # has {coachid : number of hof player taught}
        coach_player_dict = {}
        
        
        query_data = "Select coach_id,year_,team_id From coaches Where year_ >= '%s' And year_ <= '%s'"
        cursor.execute(query_data % (year1,year2))
        record_data = cursor.fetchall()
        for i in record_data:
            coach_dictionary[(i[1],i[2])] = i[0]
            coach_player_dict[i[0]] = 0
        
        
        query_1 = "Select player_name,season.year_,season.team_id From season, hall_of_fame Where season.year_ = hall_of_fame.year_ And season.player_name = hall_of_fame.name And season.year_ >= '%s' And season.year_ <= '%s' AND  hall_of_fame.year_ >= '%s' And hall_of_fame.year_ <= '%s'"
        
        cursor.execute(query_1% (year1,year2,year1,year2))
        record_player = cursor.fetchall()
        for i in record_player:
            match_team_year[(i[1],i[2])] = i[0]
        
        for key in match_team_year:
            for key_2 in coach_dictionary:
                if(key == key_2):
                    coach_player_dict[key_2.values()]+=1
        
        #gets the coach id of most taught hof players
        answer = max(coach_player_dict,key = coach_player_dict.get)
        ans = answer.replace("'","\\'")
        query_check_coach_name = "Select full_name from draft Where player_id = '%s'"
        
        cursor.execute(query_check_coach_name%(ans))
        final_answer = cursor.fetchall()
        line = str(final_answer[0]).replace("('","")
        line_1 = line.replace("',)","")
        if(len(final_answer) != 0):
            return("Player name is {} and coachid is {}.\n".format(line_1,ans))
        else:
            return ("Coachid is {}, but has not been a player\n".format(ans))
        
    
    
    
    def coach_teach_most_hof(self):
        #Which coach taught the most hall of fame players
        #returns a name or coachID
        cursor = self.conn.cursor()
        
        # has {(year,teamid): coachid}
        coach_dictionary = {}
        
        # has {(year,teamid): name of hof player}
        match_team_year = {}
        
        # has {coachid : number of hof player taught}
        coach_player_dict = {}
        
        
        query_data = "Select coach_id,year_,team_id From coaches"
        cursor.execute(query_data)
        record_data = cursor.fetchall()
        for i in record_data:
            coach_dictionary[(i[1],i[2])] = i[0]
            coach_player_dict[i[0]] = 0
        
        
        query_1 = "Select player_name,season.year_,season.team_id From season, hall_of_fame Where season.year_ = hall_of_fame.year_ And season.player_name = hall_of_fame.name "
        
        cursor.execute(query_1)
        record_player = cursor.fetchall()
        for i in record_player:
            match_team_year[(i[1],i[2])] = i[0]
        
        for key in match_team_year:
            for key_2 in coach_dictionary:
                if(key == key_2):
                    coach_player_dict[key_2.values()]+=1
        
        #gets the coach id of most taught hof players
        answer = max(coach_player_dict,key = coach_player_dict.get)
        ans = answer.replace("'","\\'")
        query_check_coach_name = "Select full_name from draft Where player_id = '%s'"
        
        cursor.execute(query_check_coach_name%(ans))
        final_answer = cursor.fetchall()
        
        if(len(final_answer) != 0):
            return("Player name is {} and coachid is {}.".format(final_answer,ans))
        else:
            return ("Coachid is {}, but has not been a player".format(ans))
    
    def seasonstat(self,player,year):
        #given year and player
        #return season detail of that player
        #if player did not have stats that year return [False] otherwise return an array of stats
        cursor = self.conn.cursor()
        player = player.replace("'","\\'")
        year = year.replace("'","\\'")
        query = "Select * From season Where player_name = '%s' and year_ = '%s'"
        cursor.execute(query%(player,year))
        season_stats = cursor.fetchall()
        if(len(season_stats) != 0):
            return(season_stats)
        else:
            return ("No season stats for this year for this player!\n")
    
    def player_draft(self,player):
        #given player name return draft college and year
        cursor = self.conn.cursor();
        p=player.replace("'","\\'")
        query = "SELECT draft_from_college, draft_year FROM draft WHERE full_name = '%s'"
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
        cursor = self.conn.cursor()
        name = name.replace("'","\\'")
        query = "Select year_ from hall_of_fame Where hall_of_fame.name = '%s'"
        if(cursor.execute(query%(name)) != NULL):
            return cursor.fetchone()
        else:
            return False



s = "SELECT d.full_name, d.player_id FROM draft as d, hall_of_fame as h WHERE d.full_name = h.name;"
#returns list of names in hall of fame
s1 = "SELECT    "