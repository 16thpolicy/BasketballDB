import database
import os

connection_string = "host='localhost' dbname='database_final' user='database_final_user' password='database_final'"

Bball = database.Basketball(connection_string)

print(Bball.player_draft("Marvin Delph"))

print("This program will tell you some specific information about basketball, players and coaches")
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
        exit_=0
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
                    print(" %d) %s"%(i,namelist[i-1]))
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
                    print(" 4) Overall PER")
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
                if(p_info_choice==1):
                    print("[input season stats here]")
                elif(p_info_choice==2):
                    print("[draft info here]")
                elif(p_info_choice==3):
                    print("[team info here]")
                elif(p_info_choice==4):
                    print("[overall per here]")
                print("returning to main menu\n")
                MM=0

    else: #coaches
        break
        #if the coach was a player
            #overall stats as a player
            #where were they drafted
            #teams they played for
        #Did they improve these teams after their first year?:
            #Difference in PER of players who were in the year before and current year 


    

    

print("\nThank you for using our program, I hope it was informative!")