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
#explore HERE^


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
        query = "SELECT MIN(year_), MAX(year_) FROM draft, coaches WHERE draft.player_id = coaches_id AND LOWER(player_id) = LOWER('%s')"

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
        query = "SELECT DISTINCT team_id AS Team FROM season WHERE Season.player_name = '%s' ORDER BY Team DESC"
        cursor.execute(query%(p))
        return cursor.fetchall()
    
    def find_overall_per(self,player):
        #given player name return overall per
        cursor = self.conn.cursor();
        p=player.replace("'","\\'")
        query = "SELECT AVG(season.player_efficiency) FROM season WHERE season.player_name = '%s'"
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

    #given coach name determine how many HOF players they have coached
    def amount_of_hof_coached(self, coach_name):
        cn = coach_name.replace("'","\\'")
        cursor = self.conn.cursor()
        query = "SELECT COUNT(hof.full_name)\
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
                WHERE LOWER(hof.full_name) = LOWER(all_p.player_name)"%(coach_name)
        cursor.execute(query)
        return cursor.fetchall()
    