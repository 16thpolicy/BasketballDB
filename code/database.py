import psycopg2
import os


class Basketball():

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    def was_coach(self, player_name):
        return False

    def was_player(self, coach_name):
        return False
    
    def searchplayers(self, player):
        if player=='0':
            return []
        return ["Player1","Player2","Player3"]
    #Which coach taught the most hall of fame players