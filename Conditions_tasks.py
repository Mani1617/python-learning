# Enter marks

# If marks >= 90 → Grade A
# If marks >= 70 → Grade B
# If marks >= 35 → Grade C
# Else → Fail
# marks =int(input('Enter your marks :'))

# if marks > 100 and marks < 0 :
#     print('Enter Valid Marks') 
# elif marks >= 90 :
#     print ('Grade A')
# elif marks >= 70 :
#     print ('Grade B')
# elif marks >= 35 :
#     print ('Grade C')
# else:
#     print('Failed')
#Write a program that takes an age as input and classifies the person into one of the following age groups:
# Child: 0-12 years
# Teenager: 13-17 years
# Adult: 18-64 years
# Senior: 65 years and older
# age =int(input('Enter Your age :'))
# if age < 0:
#     print('Enter valid age number')
# elif age >=0 and age <=12 :
#     print('child')
# elif age >=13 and age <=17 :
#     print('Teenager')
# elif age >=18 and age <=64 :
#     print('Adult')
# else:
#     print('65 years and older')
#Write a program that takes an integer as input and classifies it as positive,negative, or zero
# . Use the
# num =int(input('Enter Number:'))
# if num < 0 :
#     print ('Enter number is Negative number')
# elif num > 0 :
#     print ('Enter number is Negative number')
# else:
#     print ('Enter number is Zero')
# Create a program that checks whether a given year is a leap year or not. A
# leap year is divisible by 4, but not by 100 unless it is divisible by 400.
# year =int(input('Enter year:'))
# if year % 4 ==0 and year % 100 !=0 and year % 400 ==0 :
#     print('Given year is Leap year')
# else:
#     print ('Given year is not a leap year')
# Build a simple calculator program that takes two numbers and an operator
# (+, -, *, /) as input and performs the corresponding operation.
# num1=int(input('Enter firstnumber:'))
# num2=int(input('Enter secondnumber:'))
# operator = input ('Enter user operator to perform :')
# if operator =='+':
#     print('Adding two numbers :', num1+num2)
# elif operator =='-':
#     print('subtracting two numbers :', num1-num2)
# elif operator =='*':
#     print('multiply two numbers :', num1*num2)
# elif operator =='/':
#     if num2==0 :
#         print('Divided by Zero is Error')
#     else:
#       print('divide two numbers :', num1/num2)
# else:
#     print('Invalid char or inavlid operator')

# Create a program that calculates the final price after applying a discount.
# The program should take the original price and the discount percentage as
# input.

# price = float (input('Enter the price : ' ))
# Dsct_per = int(input('Enter Discount percentage :') )
# if Dsct_per >= 0 :
#     Disc_amount = price * Dsct_per/100
#     total_price =price-Disc_amount
#     print(f"Total bill amount is after discount : {total_price}")
# else:
#     print ('Invalid percentage')
# Write a program that calculates the Body Mass Index (BMI) using the
# formula: BMI = weight (kg) / (height (m))^2. The program should take
# weight and height as input.
# weight = float (input('Enter the weight : ' ))
# height = float(input('Enter the height:') )

# if 0 < height == 0:
#     print ('Inavlid hight or divided by zero')

# elif height >0:
#     BMI= weight / (height)**2
#     print(f'Your body BMI is {BMI}')

# x = 8
# if x % 2 == 0: result = "Even"
# else: result = "Odd"
x=9
print('Even') if x % 2 == 0 else print('odd')









