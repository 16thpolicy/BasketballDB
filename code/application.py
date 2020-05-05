import database
import os

connection_string = "host='localhost' dbname='database_final' user='database_final_user' password='database_final'"

Bball = database.Basketball(connection_string)

print("\nThis program will tell you some specific information about basketball, players and coaches!")
exit_ = 1
while(exit_):
    category = 0
    while(category == 0):
        try:
            category = int(input("Please select a category (Enter an integer): \n 1) Players\n 2) Coaches\n 3) Exit\n=> "))
            if(category not in range(1,4)):
                print("Invalid: selected number is not within range of categories\n")
                category = 0
        except:
            print("Invalid: not a number please select again\n")
    MM = 1
    if(category==3):
        exit_ = 0
        continue
    elif(category==1): #player
        player = ''
        while(player == '' and MM):
            player = str(input("\nWhich player do you want to search for? (Enter any part of a name)\n=> "))
            #remember to steralize input and change case-senitivity using Lower
            namelist = Bball.searchplayers(player) #return list of player names LIKE given string
            namelistrange = range(1,len(namelist)+1)
            if(len(namelistrange) == 0): #if there doesn't exist players
                print("Sorry I cannot find any players of similar name, try again.")
                player = ''
                continue #return to while loop to try again
            p_number = 0
            while(p_number==0 and MM):
                for i in namelistrange: #prints out names
                    print(" %d) %s"%(i,namelist[i-1][0]))
                print(" %d) Main Menu"%(len(namelist)+1))
                try: #user selects player
                    p_number = int(input("\nWhich player would you like to explore? (Enter an integer)\n=> "))
                    if(p_number == len(namelist)+1):
                        MM=0
                        continue
                    elif(p_number not in namelistrange):
                        print("Invalid: selected number is not within range of players")
                        p_number = 0
                        player = ''
                        continue
                except:
                    print("Invalid: value entered was not a number")
                    continue
                p_info_choice = 0
                #prob another while loop
                while(p_info_choice == 0 and MM):
                    print("\nWhich of these information would you like to know? (Enter an integer): ")
                    print(" 1) Enter a season for stat information")
                    print(" 2) When and where was %s drafted"%(namelist[p_number-1]))
                    print(" 3) Which team(s) %s played for"%(namelist[p_number-1]))
                    print(" 4) Was %s in the Hall Of Fame? If so what year was he inducted?" % (namelist[p_number-1]))
                    print(" 5) Main Menu")
                    try:
                        p_info_choice = int(input("=> "))
                        if(p_info_choice == 5):
                            MM=0
                            continue
                        elif(p_info_choice not in range(1,6)):
                            print("Invalid: selected number is not within range of choices")
                            p_info_choice =0
                            continue
                    except:
                        print("Invalid: value entered was not a number")
                        continue
                if(p_info_choice == 1):
                    active_range = Bball.return_range(namelist[p_number-1][0])[0]
                    player_stat_year = 0
                    while(not player_stat_year):
                        try:
                            player_stat_year = int(input("\n%s was active from %d to %d (Enter year)\n=> "%(namelist[p_number-1][0],active_range[0],active_range[1])))
                            if(not player_stat_year in range(active_range[0],active_range[1]+1)):
                                print("Invalid: selected year is not within range of choices")
                                player_stat_year=0
                        except:
                            print("Invalid: value entered was not a number")
                            continue
                    season_search = Bball.seasonstat(namelist[p_number-1][0],player_stat_year)[0]
                    print("\nIn the year %d, %s played the position of %s at the age of %s scoring %d points that season."%((player_stat_year,namelist[p_number-1][0])+season_search))                    
                    
                elif(p_info_choice == 2):
                    draft_print = Bball.player_draft(namelist[p_number-1][0])
                    print("\nCollege/High School: {} Draft Year: {}".format(draft_print[0][0],draft_print[0][1]))
                    
                elif(p_info_choice==3):
                    teams_played_on = Bball.teamsplayed(namelist[p_number-1][0])
                    if(not len(teams_played_on)-1):
                        print("\n%s only played for %s"%(namelist[p_number-1][0],teams_played_on[0][0]))
                    else:
                        print("\n%s played for:"%(namelist[p_number-1][0]))
                        for i in teams_played_on:
                            print("- %s"%(i[0]))

                elif(p_info_choice==4):
                    year = Bball.hof(namelist[p_number-1][0])
                    if(year):
                        print("\n%s was inducted into the Hall of fame in %d"%(namelist[p_number-1][0],year[0][0]))
                    else:
                        print("\n%s is not a Hall of Famer"%(namelist[p_number-1][0]))
                print("returning to main menu\n")
                MM=0

    else: #coaches
        coach = ''
        while(coach == '' and MM):
            coach = str(input("\nWhich coach do you want to search for? (Enter any part of a name)\n=> "))
            #remember to steralize input and change case-senitivity using Lower
            namelist = Bball.searchcoaches(coach) #return list of coach names LIKE given string
            namelistrange = range(1,len(namelist)+1)
            if(len(namelistrange) == 0): #if there doesn't exist players
                print("Sorry I cannot find any coaches of similar name, try again.")
                coach = ''
                continue #return to while loop to try again
            p_number = 0
            while(p_number==0 and MM):
                for i in namelistrange: #prints out names
                    print(" %d) %s"%(i,namelist[i-1][0]))
                print(" %d) Main Menu"%(len(namelist)+1))
                try: #user selects player
                    p_number = int(input("\nWhich coach would you like to explore? (Enter an integer)\n=> "))
                    if(p_number == len(namelist)+1):
                        MM = 0
                        continue
                    elif(p_number not in namelistrange):
                        print("Invalid: selected number is not within range of coaches")
                        p_number = 0
                        coach = ''
                        continue
                except:
                    print("Invalid: value entered was not a number")
                    continue 
                p_info_choice = 0
                #prob another while loop
                while(p_info_choice == 0 and MM):
                    print("\nWhich of these information would you like to know? (Enter an integer): ")
                    print(" 1) Who has %s coached in a specific season?"%(namelist[p_number-1][0]))
                    print(" 2) Which teams did %s coached? "%(namelist[p_number-1][0]))
                    print(" 3) Which Hall of Famers did %s coached?"%(namelist[p_number-1][0]))
                    print(" 4) Main Menu")
                    try:
                        p_info_choice = int(input("=> "))
                        if(p_info_choice == 4):
                            MM = 0
                        elif(p_info_choice not in range(1,4)):
                            print("Invalid: selected number is not within range of choices")
                            p_info_choice = 0
                            continue
                    except:
                        print("Invalid: value entered was not a number")
                        continue
                if(p_info_choice == 1):
                    active_range = Bball.coach_range(namelist[p_number-1][0])[0]
                    coach_year = 0
                    while(not coach_year):
                        try:
                            coach_year = int(input("\n%s was actively coaching from %d to %d (Enter year)\n=> "%(namelist[p_number-1][0],active_range[0],active_range[1])))
                            if(not coach_year in range(active_range[0],active_range[1]+1)):
                                print("Invalid: selected year is not within range of choices")
                                coach_year=0
                        except:
                            print("Invalid: value entered was not a number")
                    players_coached = Bball.players_coached_season(namelist[p_number-1][0],coach_year)
                    print("During the season of %d, %s coached:"%(coach_year,namelist[p_number-1][0]))
                    for i in players_coached:
                        print("- %s"%(i[0]))

                elif(p_info_choice == 2):
                    teams_coached = Bball.teams_coached(namelist[p_number-1][0])
                    if(len(teams_coached)==1):
                        print("\n%s only coached %s"%(namelist[p_number-1][0],teams_coached[0]))
                    elif(len(teams_coached)>1):
                        print("\n%s coached multiple teams including:"%(namelist[p_number-1][0]))
                        for x in teams_coached:
                            print("- %s"%(x))
                    else:
                        print("No data on teams Coached")

                elif(p_info_choice==3):
                    HOFs = Bball.hof_coached(namelist[p_number-1][0])
                    if(len(HOFs)==1):
                        print("\n%s only coached the Hall of Fame player %s"%(namelist[p_number-1][0],HOFs[0]))
                    elif(len(HOFs)==0):
                        print("\n%s has never coached a Hall of Fame player"%(namelist[p_number-1][0]))
                    elif(len(HOFs)>1):
                        print("\n%s has coached many Hall of Fame players including:"%(namelist[p_number-1][0]))
                        for y in HOFs:
                            print("- %s"%(y))
                        
                    
                print("returning to main menu\n")
                MM = 0
print("\nThank you for using our program, I hope it was informative!")
