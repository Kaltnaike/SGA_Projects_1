#Using the exponential operator
print('Exponential operator, Variables, Assigning user-choice Integers')
 
def exponent(x,y):
                  return 1 if y== 0 else x ** y

x = int(input("Input Base Value:"))
y = int(input("Input Exponential value:")) 

x = exponent(x,y)
print("The Answer is:" + str(x))