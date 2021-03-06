import psycopg2
import os


class Basketball():

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    def searchplayers(self, player):
        #given part of a player_name use LIKE to find all names containing '%player%'
        #returns a list of player names in alphabetical decending order
        p = player.replace("'","\\'")
        query = "Select DISTINCT player_name From season Where LOWER(player_name) LIKE LOWER('%%%s%%') ORDER BY player_name DESC"
        cursor = self.conn.cursor()
        cursor.execute(query%(p))
        return cursor.fetchall()
    
    def return_range(self, player):
        p = player.replace("'","\\'")
        query = "SELECT MIN(year_), MAX(year_) FROM season WHERE LOWER(player_name) = LOWER('%s')"%(p)
        cursor=self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def coach_range(self,coach):
        nam = coach.replace("'","\\'")
        query = "SELECT MIN(year_), MAX(year_) FROM draft, coaches WHERE draft.player_id = coach_id AND LOWER(full_name) = LOWER('%s')"%(nam)
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def searchcoaches(self,partofname):
        p = partofname.replace("'","\\'")
        query = "Select DISTINCT full_name FROM draft, coaches WHERE LOWER(full_name) LIKE LOWER('%%%s%%') AND coach_id = player_id ORDER BY full_name ASC"
        cursor = self.conn.cursor()
        cursor.execute(query%(p))
        return cursor.fetchall()
    
    def seasonstat(self,player,year):
        #given year and player
        #return season detail of that player
        #if player did not have stats that year return [False] otherwise return an array of stats
        cursor = self.conn.cursor()
        player = player.replace("'","\\'")
        # position, points
        query = "Select position, age_, points From season Where player_name = '%s' and year_ = '%d'"
        cursor.execute(query%(player,year))
        season_stats = cursor.fetchall()
        if(len(season_stats) != 0):
            return(season_stats)
        else:
            return ("No season stats for this year for this player!\n")
        #explore this^
    
    def player_draft(self,player):
        #given player name return draft college and year
        cursor = self.conn.cursor();
        p=player.replace("'","\\'")
        query = "SELECT draft_from_college, draft_year FROM draft WHERE full_name = '%s'"
        cursor.execute(query%(p))
        return cursor.fetchall()
    
    def teamsplayed(self,player):
        #given a playername return list of teams alphabetical order desc of all teams they were in
        cursor = self.conn.cursor();
        p=player.replace("'","\\'")
        query = "SELECT team_name FROM (\
        SELECT DISTINCT ON(team_id) team_id, year_ FROM season WHERE Season.player_name = '%s' ORDER BY team_id DESC\
        ) as s1, teams WHERE team_abbrev = s1.team_id AND team_year = s1.year_"
        cursor.execute(query%(p))
        return cursor.fetchall()
    
    def hof(self, name):
        #return year when they were inducted into HOF
        #else return False
        cursor = self.conn.cursor()
        name = name.replace("'","\\'")
        query = "Select year_ from hall_of_fame Where LOWER(hall_of_fame.name) = LOWER('%s')"
        cursor.execute(query%(name))
        return cursor.fetchall()

    def players_coached_season(self,coach,year):
        c = coach.replace("'","\\'")    
        s3 = "SELECT season.player_name\
            FROM (SELECT coaches.team_id, year_ \
                FROM coaches, draft \
                WHERE player_id = coach_id\
                AND year_ = %d \
                AND LOWER(full_name) = LOWER('%s')\
                ORDER BY team_id, year_) as q1, season\
            WHERE q1.year_ = season.year_\
            AND q1.team_id = season.team_id \
            ORDER BY season.player_name ASC"%(year,c)
        cursor = self.conn.cursor()
        cursor.execute(s3)
        return cursor.fetchall()
    
    def teams_coached(self,coach):
        nam = coach.replace("'","\\'")
        s = "SELECT team_name\
        FROM (SELECT DISTINCT ON(coaches.team_id) coaches.team_id,coaches.year_\
            FROM coaches,draft\
            WHERE draft.full_name = '%s' AND draft.player_id = coach_id)\
        as s, teams\
        WHERE team_abbrev = s.team_id AND team_year = s.year_"%(nam)
        cursor = self.conn.cursor()
        cursor.execute(s)
        return cursor.fetchall()


    #given coach name determine how many HOF players they have coached
    def hof_coached(self, coach_name):
        cn = coach_name.replace("'","\\'")
        cursor = self.conn.cursor()
        query = "SELECT hof.full_name\
                FROM (SELECT DISTINCT ON (season.player_name) season.player_name, coaches.team_id, coaches.year_\
                    FROM coaches, draft, season\
                    WHERE player_id = coach_id\
                    AND LOWER(full_name) = LOWER('%s')\
                    AND season.year_ = coaches.year_\
                    AND season.team_id = coaches.team_id\
                    ORDER BY season.player_name ASC)\
                as all_p,\
                    (SELECT d.full_name, d.player_id \
                    FROM draft as d, hall_of_fame as h \
                    WHERE d.full_name = h.name)\
                as hof\
                WHERE LOWER(hof.full_name) = LOWER(all_p.player_name)\
                ORDER BY hof.full_name ASC"%(coach_name)
        cursor.execute(query)
        return cursor.fetchall()
    