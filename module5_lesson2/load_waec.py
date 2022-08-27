#Import Dependecies
import sqlite3
import csv


#Create a databse connection
conn = sqlite3.connect('scores.db')

#Check
print("Score Database Created Successfully")

#Create a Cursor
cursor = conn.cursor()

#Check
print("Cursor Created Successfully")


#Create Table called waec_scores that has ten columns that accept text,integer inputs
create_table = """
CREATE TABLE waec_scores(

    Name TEXT,
    Maths INTEGER,
    English INTEGER,
    Chemistry INTEGER,
    Physics INTEGER,
    Biology INTEGER,
    Economics INTEGER,
    Civics INTEGER,
    Yoruba INTEGER,
    French INTEGER
)
"""

#cursor.execute(create_table)

#Check
print("Table Created Successfully")


#load existing csv file
with open('studentwaec.csv',"r") as opened_file:
    read_file = csv.reader(opened_file)
    
    #Skip header
    next(read_file)
    
    cursor.executemany("""
    INSERT INTO waec_scores VALUES(?,?,?,?,?,?,?,?,?,?)
    """, read_file)


print("Data Successfully loaded into the Database Table!")

#Commit to Database
conn.commit()

#close the connection
conn.close()