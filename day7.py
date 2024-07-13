# wap program to reverse a string without using slicing and typecaseting.
# string = input() #Hello
# rev=''
# i=0
# while i<len(string):
#     rev= string[i]+rev #'H'=>'e'+'H'='eH' => 'l'+'eH'= > 'leH'
#     i+=1
# print(rev)

# Wap to run infinite loop for login to Phonepe by entering correct otp.

# import random
# while True:
#     otp = random.randint(1000,9999)
#     u_otp = int(input(f"Your otp is {otp} :"))
#     if otp==u_otp:
#         print('Login Successful✅')
#         break
#     else:
#         print('Wrong OTP ❌\nEnter Again')
#     print(otp)
# print('Hello')

#
# username ='Hello'
# password ='Pass@123'

# u_username = input("Enter Username")
# if username == u_username:
#     while True:
#         u_password = input("Enter Password")
#         if u_password == password:
#             print("Login ....")
#             break
#         else:
#             print("Invalid Password...")
# else:
#     print('Invalid Username...')

# i/p : 123
# o/p : One Two Three
# l = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
# l = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
# s= input()
# # s = 1 2 3 4
# # i = 0 1 2 3
# i=0 #0,1,2,3
# while i<len(s):
#     st = s[i] # '1' # '2'
#     cint = int(st) # 1 # 2
#     print(l[cint],end=" ") #l[1]
#     i+=1
# n = input() #1122
# 1 => l[int(n[0])]

# wap to loop infinite and ask number from user store ,pos,neg until user enters 0

#start loop here
#ask integer input from user
# if it is +ve store it into pos variable
# if it is -ve store it into neg variable
# this loop will run until enter 0
# pos and neg (assignment)

# wap to print factorial of given number
# n =5
# fact = 1
# while n>0:
#     fact = fact*n # 1*5 =>5 * 4 => 20 * 3 = >60 *2 => 120 => 120*1 =>120
#     n-=1 # 5 -> 4 ->3->2->1
    
# # wap to check given number is prime or not.
# 5 => [1,5]
# 10 => [1,2,5,10]
# 11 => [1,11]
# method 1 
# n = int(input())
# i =1
# res = []
# while i<=n:
#     if n%i==0:
#         res.append(i)
#     i+=1
# if len(res) == 2:
#     print('Prime Number')
# else:
#     print('Not a Prime Number')
# print(res,len(res))

# method 2 
#prime 5 = [1,5] # 10 = [1,2,5,10]
# n = int(input("Enter the number : "))
# i=2
# count = 0
# while i<=n//2: #2<0
#     if n%i==0:
#         count = 1
#     i+=1
# if count ==0 and n!=1:
#     print('Prime Number')
# else:
#     print('Not a Prime Number')
    

