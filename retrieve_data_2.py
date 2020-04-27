import zipfile
import os
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()


#download single file Seasons_Stats
api.dataset_download_files('drgilermo/nba-players-stats','Seasons_Stats.csv')
#download single file basketball_coaches.csv
api.dataset_download_file('open-source-sports/mens-professional-basketball','basketball_coaches.csv')
#download single file basketball_draft.csv
api.dataset_download_file('open-source-sports/mens-professional-basketball','basketball_draft.csv')
#download single file basketball_hof.csv
api.dataset_download_file('open-source-sports/mens-professional-basketball','basketball_hof.csv')


with zipfile.ZipFile("Seasons_Stats.csv/nba-players-stats.zip", 'r') as zip_ref:
    zip_ref.extractall("Seasons_Stats.csv/nba-players-stats/")


#download whole file from men's pro
#api.dataset_download_file('open-source-sports/mens-professional-basketball')
#download whole file from NBA player
#api.dataset_download_files('drgilermo/nba-players-stats')
