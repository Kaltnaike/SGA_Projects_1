#Generate an array of 1 to 100 with both numbers included and find the L.C.M of even numbers
import numpy as np
#Creating a list
list_1 = list(range(1, 101))
print(list_1)

#Creating a one-dimensional array
array_1 = np.array(list_1)
print(array_1)

#Using np.arange() which includes start,stop and step value to create Even numbers of  the array
array_1 = np.arange(2,101,2)
print(array_1)

#Find the LCM of the Even number for more than two inputs using the np.lcm.reduce() to pass in the array of numbers
print("\nThe Least Common Multiple of Even Numbers in The Array : ", np.lcm.reduce(array_1))