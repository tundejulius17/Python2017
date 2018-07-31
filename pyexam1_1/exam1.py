import sqlite3
from os.path import isfile
insert_data=True
update_data=True
delete_data=True
#ids=[1000, 1001, 1002, 1003, 1004]
#names=['Parvin', 'Pedram', 'Puya', 'Parvaneh', 'Parmidas']
#salaries=[2432.6, 31256,5, 1678.6, 5213.8, 4412.9]
dbPath = 'exam1_1.db'
#Here we check whether the database file exist or not. If it
#exists, we create table employees in it
connection=sqlite3.connect("")

print('Enter match data')
teamNames = input('Enter teams names: ')
matchDate = input('Enter match date: ')
matchTime = input('Enter match time: ')
matchScore = input('Enter match score: ')

try:
    if(not isfile(dbPath)):
        print(dbPath + " does not exist!")
    else:
        connection = sqlite3.connect(dbPath)
        print("Connected to the database successfully!")
        cursor = connection.cursor()
        create_table_command="CREATE TABLE if not exists matches (teams text, date text, time text, score text)"
        #Here we send the table creating command to the database
        cursor.execute(create_table_command)
        #Here we save changes on the database permanently
        connection.commit()
        sql_command = "INSERT INTO matches(teams, date, time, score) VALUES (?, ?, ?, ?)"
        if insert_data==True:
            cursor.execute(sql_command, (teamNames, matchDate, matchTime, matchScore,))

        #Here we save changes permanently in the database
        connection.commit()

        #print("Data written to the database")
        print('Search match by teams:')
        searchTeams = input('Enter team names: ')

        #limit=3000
        #Here we query the database
        sql_query="SELECT * from matches where teams = ?";
        #sql_query = "SELECT * from matches"
        cursor.execute(sql_query, (searchTeams,))
        # Here we would print only one row in the cursor
        #print(cursor.fetchone())
        #Here we print all the content of the cursor
        #print(cursor.fetchall())
        #Here we print the query results
        for record in cursor:
            print(record)
        #Here we update the data in the database

        print('Search match by date:')
        searchDate = input('Enter date: ')

        sql_query1= "SELECT * from matches where date = ?";
        # sql_query = "SELECT * from matches"
        cursor.execute(sql_query1, (searchDate,))

        for record in cursor:
            print(record)
        '''
        name='Parvin'
        sql_update_command = "UPDATE employees SET salary=10000.0 WHERE name=?";
        cursor.execute(sql_update_command, (name,))
        connection.commit()
        print("Data after update: ")
        sql_command=sql_query="SELECT * from employees where name like ?"
        cursor.execute(sql_query, (name,))
        print(cursor.fetchone())

        #Here we remove data from the database
        sql_update_command = "DELETE from employees WHERE name= ?";
        cursor.execute(sql_update_command, (name,))
        connection.commit()
        print("Data after removing the row: ")
        sql_query = "SELECT * from employees where name like ? "
        cursor.execute(sql_query, (name,))
        print("The search result for " + name + " after deleting: " + str(cursor.fetchone()))
        '''

except Exception as e:
    print("Error: " + str(e))
finally:
    connection.close()