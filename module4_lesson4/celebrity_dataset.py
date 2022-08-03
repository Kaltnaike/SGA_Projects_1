#import SQLite3
import sqlite3


#Check that package is imported successfully
print('Successfully Imported module')

#create or connect to a database
conn = sqlite3.connect('celebs.db')

#check that database has been connected succesfully
print("Celebrity Database created successfully!") ; print(type(conn))

#create a cursor object that allows the execution of SQL Statements
cursor = conn.cursor()

#check that cursor is created successfully
print("Cursor created sucessfully \n", type(cursor))


#create a table called celebs with six columns that accept text,integer inputs
cursor.execute("""
                 CREATE TABLE celebs (
                        name text,
                        genre text,
                        num_albums integer,
                        age integer,
                        awards integer,
                        years_in_industry integer
                )
""")
                
#check that it is executed successfully
print(" Celebs database created successfully")



#insert multiple records
celebs_data = [
    ("Angie", "Trap-hop", "4", "27", "2", "6"),
    ("Bayli", "R&B", "1", "24","0", "2"),
    ("Beyonce", "R&B", "20", "40", "542", "25"),
    ("Bea Miller", "Pop-rock", "9", "23", "2","8"), 
    ("H.E.R", "Soul", "8", "25","21","11"), 
    ("Jucee Froot", "Rap", "0", "28","1","10"),
    ("Moore DH", "Afrobeats","1","22","0","3"), 
    ("Monita", "Hip-hop","1", "20", "0", "1"),
    ("Nicki Minaj","Rap","7", "39", "316", "18"),
    ("Niniola", "Afrobeats","4", "35", "6", "8"),
    ("Onuka", "Electro-folk","8", "36", "1", "9" ),
    ("Qveen Herby", "R&B","5", "36", "1", "12"),
    ("Saint jhn", "Hip-hop","3", "35", "0", "12"),
    ("Saweetie", "Hip-hop","3", "29", "4", "6"),
    ("Shygirl", "Rap","4", "29", "1", "6"),
    ("Summer Walker", "Soul","2", "26", "5", "5"),
    ("SZA", "R&B","1", "32", "11", "11"),
    ("Tems", "Afrobeats","2", "27", "14", "4") ,
    ("Tierra Whack", "Rap","4", "26", "2", "11"),
    ("Zheani", "Rap","5", "29", "0", "3")
    
]


cursor.executemany( 
"""
INSERT INTO celebs
VALUES(?, ?, ?, ?, ?, ?)
""",

celebs_data

)

#Check
#print("Inserted celebs_data into celebs database!")

cursor.execute(
    """
    SELECT * FROM celebs
    """
)

items = cursor.fetchall()
#print(items)

#format outputs to display in a tabular form
print("Name"+ "\t\tGenre"+ "\t\tnum_albums" "\tAge"+ "\tAwards" +"\t\tyears_in_industry \n"  f"{'.' * 100}") 

# #loop through the items
for item in items:
    name, genre, num_albums,age, awards,years_in_industry = item
    print(f"{name:16}{genre:14}{num_albums:5}{age:15}{awards:10}{years_in_industry:16}")


#Most Decorated Celebrity
def most_decorated_celebrity():
        query= """
        SELECT name
        FROM celebs
        WHERE awards = (SELECT MAX(awards)
                   FROM celebs)
        """
        print(f"This is The Most Decorated Celebrity who has amassed different accolades over the years!") 
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)
        
most_decorated_celebrity()

#Oldest Celebrity
def oldest_celebrity():
        query= """
        SELECT name
        FROM celebs
        WHERE age = (SELECT MAX(age)
                   FROM celebs)
        """
        print(f"This is The Oldest Celebrity and still slaying it!")
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)
        
oldest_celebrity()

#Celebrity with the longest years in the industry
def longest_years_in_industry():
        query= """
        SELECT name
        FROM celebs
        WHERE years_in_industry = (SELECT MAX(years_in_industry)
                   FROM celebs)
        """
        print(f"This Celebrity has been in the Industry for years! Contributing,Impacting and getting the industry where it is today!")
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)

longest_years_in_industry()
        
#Celebrity with the least number of albums
def least_num_albums():
        query= """
        SELECT name
        FROM celebs
        WHERE num_albums = (SELECT MIN(num_albums)
                   FROM celebs)
        """
        print(f"Hey Rookie,Your Singles are fire can't wait for your Debut Album!")
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)

least_num_albums()

#Most Popular genre of music amongst all celebrities in the dataset
def most_popular_genre():
        query= """
        SELECT genre,
         COUNT(genre) AS `value_occurrence` 
         FROM celebs
         GROUP BY genre
         ORDER BY `value_occurrence` DESC
         LIMIT  1;
        """
        print(f"The Most Popular Genre Trending Among the Amazing Talents!")
        cursor.execute(query)
        items = cursor.fetchall()
        print(items)

most_popular_genre()



#commit to database
conn.commit()

#close your connection
conn.close()