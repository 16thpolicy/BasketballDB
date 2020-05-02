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
        return False
    
    def seasonstat(self,player,year):
        #given year and player
        #return season detail of that player
        #if player did not have stats that year return [False] otherwise return an array of stats
        return [False]
    
    def player_draft(self,player):
        #given player name return draft college and year
        return ['RPI',2020]
    
    def teamsplayed(self,player):
        #given a playername return list of teams alphabetical order desc of all teams they were in
        return []
    
    def find_overall_per(self,player):
        #given player name return overall per
        return 2

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