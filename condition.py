# while True:
#  marks =int (input("Enter Marks you got :" ))
#  if marks >=80:
#     print("your passed in A Grade")

#  elif marks>=35 :
#     print("your passed in B Grade")
#  else:
#     print("you failed")

# number =0
# if number >0:
#     print('Postive number')
# else:
#     print('Number is negative number')

# temperature = 30

# if temperature >30:
#     print('Hot Weather')
# else:
#     print('Normal Weather')
# browser = "chrome"
# if browser=="chrome":
#      print ("Launching Chrome Browser")
# else:
#       print ("Unsupported Browser")
# # if browser is chrome
# # print "Launching Chrome Browser"
# # else
# # print "Unsupported Browser"
# username = input("Enter Username :")
# password = input ("Enter password :")
# otp = input ("Enter OTP :")
# if username == "mani123":
#     if password == "123456":
#         if otp == "145":
#             print("Login successfull ")
#         else :
#             print ("invalid OTP")
#     else:
#         print("Invalid password ")
# else:
#     print("Invalid Username")
#Write a Python program that takes a character as input and checks whetherit is a vowel or not. Use theif-else statement.

ch =input("Enter user input char :").lower()
vowel=("a","e","i","o","u")
if len(ch) > 1 :
    print('Invalid input')
elif not ch.isalpha():
    print('Emter alphabets only ')
elif len(ch)==1 and ch in vowel:
    print ("Enter character is vowel")
else:
    print("Enter character is consonant")


    
