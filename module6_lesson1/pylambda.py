#Create a list between 5.5 and 20.5
nums = [5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0,10.5,11.0,11.5,12.0,12.5,13.0,13.5,14.0,14.5,15.0,15.5,16.0,16.5,17.0,17.5,18.0,18.5,19.0,19.5,20.0,20.5]
print("Original list of Floats:")
print(nums)

#Using the lambda function count the even and odd numbers in the list
even_nums = list(filter(lambda x: (x % 2 == 0), nums))
odd_nums = list(filter(lambda x: (x % 2 != 0), nums))
print("{0} even numbers and {1} odd numbers in the nums list.".format(len(even_nums), len(odd_nums)))

#Using the lambda function that square and cube every number in the list
print("\nSquare the numbers in the list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

print("\nCube the numbers in the list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)