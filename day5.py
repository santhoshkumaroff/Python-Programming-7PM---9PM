# # wap to print the last value of a list only if it is having a palindrome and when last string starting with vowel.
# #i/p
# l = [1,2,3,'eye']
# #o/p 'eye'
# # check last value type if it is string then check
# # that string is palindrome or not.
# # check last value first char =[0] if that char present in vowels 
# #then print 'eye'
# #positive of l 0,1,2,3
# # negative index   -4,-3,-2,-1
# # print(l[-1],type(l[-1]))
# #method 1
# if type(l[-1]) == str:
#     if l[-1] == l[-1][::-1]:
#         if l[-1][0] in 'AEIOUaeiuo':
#             print(f"{l[-1]}")
#         else:
#             print("Not a vowel")
#     else:
#         print("Not a palindrome")
# else:
#     print("Last value type is not a string")
        
# # method 2
# if (type(l[-1]) == str) and (l[-1] == l[-1][::-1]) and (l[-1][0] in 'AEIOUaeiuo'):
#     print(l[-1])

# wap to consider a character input if it is uppercase convert it into lowercase,if it is lowercase convert into uppercase,if it is digit print the remainder when divided by 3,else if it special character print ascii value
# print(ord('A'),ord('a'))
# print(ord('A')-ord('a'))
# char = 'A'
# char1 = 'a'
#1
# print(f"Uppercase to lower case {char} --> {chr(ord(char)+32)}")
# #2
# print(f"Lowercase to upper case {char1} --> {chr(ord(char1)-32)}")
#3 convert that character to int then %3 - to get a remainder
#4 print ascii value for special character
# print(chr(ord(char)+32))
char = input()
if 'A'<=char<='Z':
    print(chr(ord(char)+32))
elif 'a'<=char<='z':
    print(chr(ord(char)-32))
elif '0'<=char<='9':
    print(int(char)%3)
else:
    print(ord(char))
    
# wap to print fizz if the given number is multiple of 3,print buzz if the given number is multiple of 5 and print fizz buzz if the number is multiple of both 3 and 5.

# wap to check the age of a person and print a different message depending on their age.
# age>=60 - senior citizen
# age>=18 - adult
# age<18 - teenager

age = int(input())
if age>=60:
    print("Senior citizen")
else:
    if age>=18:
        print("adult")
    else:
        print("Teenager")
        
# wap to calculate two number if user enter 1 - add, if 2 - sub ,3 - multiply, 4 - division,5 - power
#take one input from user as a integer
# if num ==1
# add two numbers
# elif num ==2
# sub two number
n1=int(input())
n2=int(input())
option = int(input("Enter option : "))
if option ==1:
    print(f"add = {n1+n2}")
elif option==2:
    print(f"sub - {n1-n2}")
elif option == 3:
    print(f"mul {n1*n2}")
elif option == 4:
    print(f"div {n1/n2}")
elif option == 5:
    print(f"pow {n1**n2}")
else:
    print("Invalid option")
# wap to check balance ,deposit amount,withdraw.
balance = 10000
option = int(input())
if option ==1:
    print(f"balance : {balance}")
elif option ==2:
    d_amt = int(input())
    print(f"current balance is {balance+d_amt}")
elif option == 3:
    w_amt = int(input())
    print(f"Current balance is {balance-w_amt}")
else:
    print("Invalid Option..")
    
# if enter 1 just show the balance
# if enter 2 for deposit amount after that just print balance
#if enter 3 for withdraw , print balance
