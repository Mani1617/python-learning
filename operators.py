'''a=10
b=3
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponentiation = a ** b
#floor_division = a // b
print(addition,subtraction,multiplication,division,remainder,floor_division,exponentiation)

x = 5
x += 3 # equivalent to x = x + 3
y = 10
y *= 2 # equivalent to y = y * 2
z=10
z-=5
print(x, y,z)

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(id(a is b)) # True
print(id(a is c)) # True
A=10
B=5
A,B=B,A
print (A,B)
list_example = {1, 2, 3, 4, 5}

print(3 in list_example) # True
print(6 not in list_example) # True
name = "John"
age = '30'
# Using f-string for formatting
print(f"My name is {name} and I am {age} years old.")

Name=input("Enter your name" )
Age=input("Enter Your age")
print(f"Welcome to {Name} and your age is {Age}")
numbers=[1,2,3,4,5,6,7,8,9,10]
print(5 in numbers)
print(15 not in numbers)'''

'''Write a Python program to calculate the area of a rectangle using the given
formula: area = length * width . Take the values of length and width as inputs from
the user
length =int (input("Enter area length: "))
#length=int(length)
Width=int (input("Enter area width: "))
#Width=int(Width)
area=(length * Width)
print(area)'''

#Write a Python program to demonstrate incrementing and decrementing a variable

'''Var=10
Var+=5
Var-=5

print("incrementing value Var=Var+5 :",Var)
print("decrementing value Var=Var-5 :",Var)'''
#Write a Python program to convert temperature from Celsius to Fahrenheit. The
#formula for conversion is: F = (C * 9/5) + 32 . Take the temperature in Celsius as


'''celsius=float(input("Enter the Body Temparature : ") )
Fahrenheit= (celsius * 9/5) + 32 
print(f"Converted Value is {Fahrenheit}")'''
#Write a Python program to calculate the simple interest given the principal
#amount, rate, and time (in years).

'''amount=int(input("Enter the principal Amount :"))
rate=int(input("Enter the Rate of rupees :")) 
time=int(input("Enter the total years  :")) 
time_inmonths=time * 12 
intrest_amount= (amount * rate/100)*time_inmonths
print(intrest_amount)'''
#Write a Python program to concatenate two strings and display the result. The
#strings should be taken as input from the user.
'''username=input("Enter the Username :")
Surname=input("Enter the Surname :")
print(f"Myname is {username} and my Surname is {Surname}")
print(username +" " +Surname)'''
'''#Write a Python program to convert a distance from kilometers to miles.

uservalue = int(input("Enter user kilometers: "))
Kilometer=0.621371
mile=uservalue * Kilometer
print(f"Converted Kilometers into miles :{mile}")'''




