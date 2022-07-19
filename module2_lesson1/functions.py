# Python program to find the maximum number among any three input numbers from user using functions.

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))

def max_num_1( x, y ):
    if x > y:
        return x
    return y
def max_num( x, y, z ):
    return max_num_1( x, max_num_1( y, z ) )
print(max_num(x,y,z))