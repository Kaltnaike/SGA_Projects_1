#Creating a python program to generate and print a Dictionary containing keys ranging from 5 to 15
#creating a Dictionary called squares with key:value pairs as num:squares
squares = {}
for x in range(5,16):
 #Values should be the squares of the keys   
    squares[x] = x**2
print(squares)  
