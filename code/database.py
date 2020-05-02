import psycopg2
import os


class Basketball():

    def __init__(self, connection_string):
        self.conn = psycopg2.connect(connection_string)

    #Which coach taught the most hall of fame players