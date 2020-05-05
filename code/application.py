import database
import os

connection_string = "host='localhost' dbname='database_final' user='database_final_user' password='database_final'"

Bball = database.Basketball(connection_string)

print(Bball.players_coached_season("ISIAH THOMAS",2006))
print(Bball.amount_of_hof_coached("ISIAH THOMAS"))


print("This program will tell you some specific information about basketball, players and coaches!")
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
                    print(" 3) Which teams %s played for"%(namelist[p_number-1]))
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
                            if(not player_stat_year in range(active_range[0],active_range[1])):
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
                player = ''
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
                    print(" 1) Enter a season for stat information about the coach as a player")
                    print(" 2) When and where was %s drafted"%(namelist[p_number-1]))
                    print(" 3) What teams did %s play on? "%(namelist[p_number-1]))
                    print(" 4) Which coach taught the highest number of hall of fame players?")
                    print(" 5) Was %s in the Hall Of Fame? If so what year was he inducted?" % (namelist[p_number-1]))
                    print(" 6) Main Menu")
                    try:
                        p_info_choice = int(input("=> "))
                        if(p_info_choice == 6):
                            MM = 0
                            continue
                        elif(p_info_choice not in range(1,7)):
                            print("Invalid: selected number is not within range of choices")
                            p_info_choice =0
                            continue
                    except:
                        print("Invalid: value entered was not a number")
                        continue
                if(p_info_choice == 1):
                    year = str(input("\nWhat season year do you want to search for? (Enter year)\n=> "))
                    coach_name = str(namelist[p_number-1])[1:-1]
                    coach_name_replace = coach_name.replace(",","")
                    final_coach_name = coach_name_replace.replace("'","")
                    
                    season_search = Bball.seasonstat(final_coach_name,year)
                    print("[{}]".format(season_search))
                    
                elif(p_info_choice == 2):
                    coach_name = str(namelist[p_number-1])[1:-1]
                    coach_name_replace = str(coach_name).replace(",","")
                    final_coach_name = coach_name_replace.replace("'","")
                    draft_print = Bball.player_draft(final_coach_name)
                    print("College/High School: {} Draft Year: {}".format(draft_print[0][0],draft_print[0][1]))
                    
                elif(p_info_choice==3):
                    coach_name = str(namelist[p_number-1])[1:-1]
                    coach_name_replace = coach_name.replace(",","")
                    final_coach_name = coach_name_replace.replace("'","")
                    teams_played_on = Bball.teamsplayed(final_coach_name)
                    print("Played on {} team(s)! Teams {} played on ".format(len(teams_played_on),final_coach_name))
                    for i in range(len(teams_played_on)):
                        ans = str(teams_played_on[i]).replace("('","")
                        answer = ans.replace("',)","")
                        print("{}".format(answer))
                        
                elif(p_info_choice==4):
                    ans = Bball.coach_teach_most_hof()
                    print(ans)
                elif(p_info_choice==5):
                    year1 = str(input("\nStarting year? (Enter year)\n=> "))
                    year2 = str(input("\nEnding year? (Enter year)\n\n=> "))
                    ans = Bball.coach_teach_most_hof_year(year1,year2)
                    print(ans)
                    
                elif(p_info_choice==6):
                    print("[overall per here]")
                    
                print("returning to main menu\n")
                MM = 0
        
        #if the coach was a player
            #overall stats as a player
            #where were they drafted
            #teams they played for
        #Did they improve these teams after their first year?:
            #Difference in PER of players who were in the year before and current year


    

    

print("\nThank you for using our program, I hope it was informative!")
