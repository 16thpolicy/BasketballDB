import psycopg2
import csv

connection_string = "host='localhost' dbname='database_final' user='database_final_user' password='database_final'"

# TODO add your code here (or in other files, at your discretion) to load the data


def main():
    # TODO invoke your code to load the data into the database
    print("Loading data")
    
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    with open('datasets/basketball_coaches.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO coaches VALUES (%s, %s, %s, %s,%s, %s, %s, %s, %s)",j)
    i.close()
    conn.commit()
    
    with open('datasets/basketball_draft.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO draft VALUES (%s, %s, %s, %s,%s, %s,%s, %s,%s,%s,%s)",j)
    i.close()
    conn.commit()
    
    with open('datasets/basketball_hof.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO hall_of_fame VALUES (%s, %s, %s, %s)",j)
    i.close()
    conn.commit()
    
    with open('datasets/Seasons_Stats.csv','r') as i:
        reader = csv.reader(i)
        next(i)
        for j in reader:
            cursor.execute("INSERT INTO season VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)",j)
    i.close()
    conn.commit()
    
    
    

    query_1 = "Select * from draft LIMIT 1"
    cursor.execute(query_1)
    print(cursor.fetchall())
    
    # example of fetching data
    #print("finish loading data")
    #query = "Select * from season Where season.year_ ='2017'"
    #cursor.execute(query)
    #rows = cursor.fetchall()
    #for i in rows:
    #    print(i,"\n")

    conn.close()
if __name__ == "__main__":

    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute(open("schema.sql", "r").read())
    conn.commit()
    main()