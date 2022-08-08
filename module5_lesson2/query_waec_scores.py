# Importing SQLite3
import sqlite3

#Connect to Database
conn = sqlite3.connect("scores.db")

#Create Cursor
cursor = conn.cursor()

#Query items From Scores Database
cursor.execute("""SELECT * FROM waec_scores""")

items = cursor.fetchall()
# print(items)

#Which Student Scored Highest in Maths
def max_math():
    query = """
    SELECT Name
    FROM waec_scores
    WHERE Maths = (SELECT MAX(Maths) 
    FROM waec_scores)
    """
    print('This Student Scored Highest in  Maths!')
    cursor.execute(query)
    items = cursor.fetchall()
    print(items)
max_math()

#Which Student Scored Lowest in English
def min_english():
    query = """
    SELECT Name
    FROM waec_scores 
    WHERE english = (SELECT MIN(English) 
    FROM waec_scores)
    """
    print('This Student Scored Lowest in English!')
    cursor.execute(query)
    items = cursor.fetchall()
    print(items)
min_english()

#Average score of Students in Maths
def avg_math():
    query = """
    SELECT AVG(Maths)
    FROM waec_scores
    """
    print('This is the Average Score of Students in Maths!')
    cursor.execute(query)
    items = cursor.fetchall()
    print(items)
avg_math()

# Average Score of Student in English
def avg_english():
    query = """
    SELECT AVG(English)
    FROM waec_scores
    """
    print('This is the Average Score of Students in English!')
    cursor.execute(query)
    items = cursor.fetchall()
    print(items)
avg_english()

# Best Performing Student in across all nine subjects in terms of overall scores
def best_overall():
    query = """
    SELECT * 
    FROM waec_scores
    WHERE (Maths+English+Chemistry+Physics+Biology+Economics+Civics+Yoruba+French)=(SELECT MAX(Maths+English+Chemistry+Physics+Biology+Economics+Civics+Yoruba+French)
    FROM waec_scores)
    """
    print('Best Performing Student who Aced all Subjects!')
    cursor.execute(query)
    items = cursor.fetchall()
    print(items)
best_overall()

#  Best Performing Student in across all nine subjects in terms of average scores
def best_avg():
    query = """
    SELECT *
    FROM waec_scores
    WHERE (Maths+English+Chemistry+Physics+Biology+Economics+Civics+Yoruba+French)=(SELECT AVG(Maths+English+Chemistry+Physics+Biology+Economics+Civics+Yoruba+French)
    FROM waec_scores)
    """
    print('Best Performing Student who passed all Subjects on Average!')
    cursor.execute(query)
    items = cursor.fetchall()
    print(items)
best_avg()

# commit the changes
conn.commit()

# close the connection
conn.close()