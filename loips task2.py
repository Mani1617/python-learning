# Write a Python program that calculates and prints the sum of the squares of
# numbers from 1 to 5 using a
# for loop.
# sum=0
# for i in range (1,6):
#     sum=sum+i**2
#     i+=1
#     #print(sum)
# print(sum)
# Write a Python program that uses a
# while loop to print a countdown from 5 to 1.
# i=5
# while i<=5:
#     if i==0:
#         break
#     else :
#         print(i)
#     i-=1
# Write a Python program to print the multiplication table for a user-specified
# number using a nested for loop
#num=int(input('Enter user speciaied number for Table:'))
# while num>0:
#     for i in range (1,11):
#         print(f'{num} * {i} = ', num * i)
# #     break
# # for j in range(1,2):
# #     for i in range (1,11):
# #         print(f'{num} * {i} = ', num * i)

# # *
# # * *
# # * * *
# # * * * *
# # for i in range(1, 5):

# #     for j in range(i):

# #         print("*", end=" ")
# # print()
# #     print()
# # for i in range(1,6):
# #     print(i, end=" ")
# # for i in range(1,6):
# #     print(i, end=", ")
# # for i in range(1, 5):

# #     for j in range(i):

# #        print("*", end=" ")
# # for i in range(1, 5):

# #     for j in range(i):

# #         print("*", end=" ")

# #     print()

# # for i in range(1, 5):
   
# #    for j in range(i):

# #      print(i, end=" ")

# #    print()
# # for i in range(1, 5):
   
# #    for j in range(1,i+1):

# #      print(j, end=" ")

# #    print()

# num = 1

# # for i in range(1, 5):

# #     for j in range(i):

# #         print(num, end=" ")

# #         num += 1

# #     print()

    
# # for i in range(1, 4):
   
# #   for j in range(1, i+1):

# #     print(j, end=" ")

# #   print()

# # for i in range(1, 4):
   
# #   for j in range(i):

# #     print(j+1, end=" ")

# #   print()
# num=65
# # A
# # A B
# # A B C
# # A B C D

# # for i in range(1, 5):
   
# #    for j in range(i):

# #      print(ch(num), end=" ")
#        num+=1

# #    print()
# print(chr(65))

for i in range(1, 5):

    for j in range(i):

        print(chr(65 + j), end=" ")

    print()
