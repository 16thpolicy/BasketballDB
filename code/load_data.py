import psycopg2
import csv

connection_string = "host='localhost' dbname='database_final' user='database_final_user' password='database_final'"

# TODO add your code here (or in other files, at your discretion) to load the data


def main():
    # TODO invoke your code to load the data into the database
    print("Loading data")
    
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    
    #Load in from basketball draft csv
    with open('datasets/basketball_draft.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            j[5]=j[5]+" "+j.pop(6)
            cursor.execute("INSERT INTO draft VALUES (%s, %s, %s, %s,%s, %s, %s,%s,%s,%s)",j)
    i.close()
    conn.commit()
    
    #Load in from basketball hof
    with open('datasets/basketball_hof.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO hall_of_fame VALUES (%s, %s, %s, %s)",j)
    i.close()
    conn.commit()
    

    #might Need schema which connects coachID with Coach full names HERE!!!!


    #Load in from coaches csv
    with open('datasets/basketball_coaches.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO coaches VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)",j)
    i.close()
    conn.commit()

    #Load in from Seasons Stats
    with open('datasets/Seasons_Stats.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            if(j[1].isalnum()):
                j[2] = j[2].replace("*","")
                if(not j[9].isalnum()):
                    j[9] = 0
                cursor.execute("INSERT INTO season VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",j)
    i.close()
    conn.commit()
    
    
    

    # query_1 = "Select * from draft"
    # cursor.execute(query_1)
    # print(cursor.fetchone())
    
    # example of fetching data
    #print("finish loading data")
    # query = "Select * from season Where season.year_ ='2017'"
    # cursor.execute(query)
    # rows = cursor.fetchone()
    # print(rows)

    conn.close()
if __name__ == "__main__":

    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(open("schema.sql", "r").read())
    conn.commit()
    
    main()
