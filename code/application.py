import database
import os

connection_string = "host='localhost' dbname='database_final' user='database_final_user' password='database_final'"

Bball = database.Basketball(connection_string)

print("This program will tell you some specific information about basketball, players and coaches")
category = 0
exit_ = 1
while(exit_):
    while(category == 0):
        try:
            category = int(input("Please select a category: \n 1) Players\n 2) Coaches\n 3) Exit\n(Enter an integer): "))
            if(category not in range(1,4)):
                print("Invalid: selected number is not within range of categories\n")
                category = 0
        except:
            print("Invalid: not a number please select again\n")
            category = 0

    if(category==3):
        exit_=0
        continue
    elif(category==1): #player
        break
        #which season stats
        #where player was drafted
        #teams they played for
        #did they become a coach

    else: #coaches
        break
        #if the coach was a player
            #season stats as a player
            #where were they drafted
            #teams they played for
        #Did they improve these teams after their first year?:
            #Difference in PER of players who were in the year before and current year 


    

    

print("\nThank you for using our program, I hope it was informative!")