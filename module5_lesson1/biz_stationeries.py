#import SQLite3
import sqlite3


#Check that package is imported successfully
print('Successfully Imported module')

#create or connect to a database
conn = sqlite3.connect('Biz_stationeries.db')

#check that database has been connected succesfully
print("Biz-Stationeries Database created successfully!") ; print(type(conn))

#create a cursor object that allows the execution of SQL Statements
cursor = conn.cursor()

#check that cursor is created successfully
print("Cursor created sucessfully \n", type(cursor))

#Create an Inventory Table that has 10 items with their cost price,quantity in stock. Give each item an ID
cursor.execute("""
                 CREATE TABLE stationeries (
                        objectID integer,
                        name text,
                        cost_price integer,
                        quantity_in_stock integer
                )
""")


#check that it is executed successfully
print("Stationeries table created successfully")



#insert multiple records into stationeries table
stationeries_data = [
    ("1", "Stapler", "5000", "25"),
    ("2", "Pen", "100","200" ),
    ("3", "Paperclip", "250", "50"),
    ("4", "Eraser", "30", "100"),
    ("5", "Pencil", "50", "300"),
    ("6", "Envelope", "20", "75"),
    ("7", "Marker", "150", "80"),
    ("8", "Notepad", "120", "40"),
    ("9", "Notebook", "300", "60"),
    ("10", "Scissor", "350", "65")
]

cursor.executemany( 
"""
INSERT INTO stationeries
VALUES(?, ?, ?, ?)
""",

stationeries_data

)

#Check
print("Inserted stationeries_data into Biz-Stationeries database!")

cursor.execute(
    """
    SELECT * FROM stationeries
    """
)

items = cursor.fetchall()
#print(items)

#format outputs to display in a tabular form
print("ObjectID"+ "\tName"+ "\t Cost Price(naira)""\tQuantity in Stock"+ "\n"  f"{'.' * 80}") 

# #loop through the items
for item in items:
    objectID, name, cost_price, quantity_in_stock = item
    print(f"{objectID:5}         {name:16}{cost_price:9} {quantity_in_stock:13}")


#Items to restock
def restock_items():
     query ="""
     SELECT name,
     CASE
     WHEN quantity_in_stock > 70 THEN 'Moderate Quantity in Stock'
     WHEN quantity_in_stock < 70 THEN 'Restock Products'
     ELSE 'Get New products'
    END
    FROM stationeries;
     """
     cursor.execute(query)
     items = cursor.fetchall()
     print(items)
restock_items()

#items sufficient from highest to lowest cost price
def sufficient_items_desc_cost_price():
     query ="""
     SELECT * FROM stationeries
     WHERE quantity_in_stock > 70
     ORDER BY cost_price DESC;
     """
     cursor.execute(query)
     items = cursor.fetchall()
     print(items)
sufficient_items_desc_cost_price()

#commit to database
conn.commit()

#close your connection
conn.close()



