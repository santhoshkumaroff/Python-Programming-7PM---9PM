# # wap to print all the characters of a string
# string = 'HelloBye' # 0 1 2 3 4 5 6 7 8
# i=0
# while i<len(string):
#     print(string[i],end=" ")
#     i+=1

# # char = 'PAYBTCHCODN' #P-0,Y -2,T - 4,H - 6,O-8,N-10
# # O/P : PYTHON
# char = 'PAYBTCHCODN'
# i=0
# while i<len(char):
#     if i&1==0:
#         print(char[i],end=" ")
#     i+=1

# wap to find the length of given string without using len() and typecasting.
# char = 'PAYBTCHCODN'
# i=0
# # count =0
# while i<len(char):
#     # count+=1
#     i+=1
# print(i)

# wap to extract all the vowels present in a given string.
# st ='Abcdef'
# string=input("Enter string : ")
# vowel=''# 'A'+'e'='Ae'
# i=0
# while i< len(string):
#    if string[i] in 'AEIOUaeiou':
#        vowel+=string[i]
#    i+=1
# print(vowel) 

# wap to extract uppercase,lowercase,digit,special character.
# i/p :char='HeLlo@123'
# o/p : uppercase : HL,lowercase : elo,digit - 123,spl char - @
# char='HeLlo@123'
# i=0
# upper=''
# lower =''
# digit=''
# splchar=''
# while i<len(char):
#     if 'A'<=char[i]<='Z':
#         upper+=char[i]
#     elif 'a'<=char[i]<='z':
#         lower+=char[i]
#     elif '0'<char[i]<='9':
#         digit+=char[i]
#     else:
#         splchar+=char[i]
#     i+=1
# print(f'uppercase : {upper}\nlowercase : {lower}\ndigit : {digit}\nspecial char : {splchar}')

# i/p :  
# char='HeLlo@123'
# # o/p : hElLO@123
# output=''
# i=0
# while i<len(char):
#     if 'A'<=char[i]<='Z':
#         output+=chr(ord(char[i])+32)
#     elif 'a'<=char[i]<='z':
#         output+=chr(ord(char[i])-32)
#     elif '0'<char[i]<='9':
#         output+=char[i]
#     else:
#         output+=char[i]
#     i+=1
# print(output)

# wap to print all factors of a given number.
# n=10
# 1,2,5 => 1+2+5 == given number
# wap to check the number is perfect number or not.
# n = 6 =>1,2,3 =>1+2+3 == n
# n = int(input())
# sum = 0
# i=1
# while i<n:
#     if n%i==0:
#         sum+=i
#     i+=1
# if n == sum:
#     print('Perfect number')
# else:
#     print('Not a Perfect number')

# wap to reverse the given number without using slicing and typecasting.
# i/p : n = 123
# o/p : 321
# n!=0 or n<0 # 12!=0
# rev = 0 # 3 
# ld = n%10 => 123%10 = > 3 =>12%10 => 2
# rev = rev*10+ld # 3*10 =>30+2>32
# n = 123//10 = >12


# i/p : n = 123

n = int(input())
rev=0 #3
while n!=0: #12!=0 #1!=0
    lastdigit = n%10 #3 #12%10=>2 #1%10 =>1
    rev = rev*10+lastdigit #0*10+3 =>3 #  3*10+2 >30+2 = >32 # 32*10+1 =>320+1 =>321
    n=n//10 # 123//10 =>12 =>1 #1//10 =>0
if n == rev:
    print(f"Yes the given {n} is palindrome")
else:
    print(f"{n} is not a palidrome")
#wap to check given number is palindrome or not.

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
    
# wap to print fibonacci series upto n
# 10 fibonacci series - 0 1 1 2 3 5 8 13 21 34
# start = 0
# prev = 1 
# next = start + prev # 1

# method 1 

# n = 10
# start =0
# prev = 1
# next = 0
# while n>0:
#     print(next,end=" ")
#     start,prev=prev,next # swapping numbers start <-> prev and prev <-> next
#     next = start+prev # adding previous two numbers to get next number
#     n-=1 #updation
    
# method 2

# n=10-2
# l= [0,1] # already have 2 numbers
# while n>0:
#     next = l[-1]+l[-2] #prev + #start 1 + 0 => 1
#     l+=[next] # [0,1,1] 3rd number it taken as 1 number
#     n-=1
# print(l)

# write a program to print factorial of given number.

# N =5

# wap to check given number is strong number or not.
# num = 145 # 1! + 4! + 5! or 5! + 4! + 1!  == 145 => strong number

# 145 => 5 145%10 => 5
# n = int(input("Enter Number : "))
# n1 =n
# sum =0
# while n!=0: #14 !=0 1 #1
#     ld = n%10 # 14%10 =>? 1%10
#     fact=1
#     while ld>0: #4 #3 #2 #1
#         fact = fact*ld # 1 * 4 => 4 * 3=>12 *2 = > 24 * 1 => 24
#         ld-=1 # 3 #2 #1
#     sum+=fact #120 + 24 = > 144 + 1 => 145
#     n = n//10 # 145//10 => 14 => 14//10 1//10 => 0
# if n1==sum:
#     print(f'Yes {n1} {sum} Strong number')
# else:
#     print('Not a Strong Number')
    
# wap to check given number is amstrong number or not.
# n = 153 
# length of given number and store it into one variable l = len(str(n)) = > 3
# 1cube3 or 1**3 + 5 **3 + 3**3 = 153

# n = int(input("Enter Number : ")) #153
# l = len(str(n))
# num = n
# sum = 0
# while n!=0: #15!=0 #1!=0 False loop will end
#     ld = n%10 # 3 #15%10 => 5 #1
#     sum+= ld**l # sum = sum+ld**l => 0+3**3=>27 + 5**3 => 125 +27 => 152 + 1**3 => 152+1=> 153
#     n//=10 # or n=n//10 153//10 => 15//20 => 1//10 => 0
# if num == sum:
#     print(f'Yes {num} is Amstrong Number')
# else:
#     print(f"No {num} is Not an Amstrong Number")
    
# wap to guess given number
# import random
# random_number = random.randint(1,100)
# while True:
#     guessing_number = int(input("Enter Number : "))
#     if guessing_number>random_number:
#         print(f"your {guessing_number} is greater than random number")
#     elif guessing_number<random_number:
#         print(f"Your {guessing_number} is smaller than random number")
#     else:
#         print(f'Correct the number is {random_number}')
#         break
    
    
# i/p = ["Hai","Hello","Good"]
# o/p = > {"Hai":3,"Hello":5,"Good":4}
# l = ["Hai","Hello","Good"]
# i = 0
# out ={}
# while i<len(l): # 0 # 1 #2
#     out[l[i]]=len(l[i]) # out['Hai'] = 3 # out[l[1]]=> out["Hello"] = 5 = > out[l[i]] = > out["Good"] = 4
#     i+=1
# print(out)

# i/p : l = ["Hai",20,46.7,"New","Good","Py"]
# o/p : {"Hai":"Hi","New":"Nw","Good":"Gd","Py":"Py"}

# i = 0
# out = {}
# type of value which is equal to str
# add it to out key is "Hai" and value = l[i][0] + l[i][-1]
# i+=1
# print out
# l = ["Hai",20,46.7,"New","Good","Py"]
# i=0
# out ={}
# while i<len(l): # 0 # 1 #2 # 3 #4 #5
#     if type(l[i]) == str: #l[0] => "Hai" == str # yes it is string type(20) == str # type(46.7) == str #New => type("New")==str
#         out[l[i]] = l[i][0] + l[i][-1] # => out["Hai"] = "Hai"[0] => "H" + "Hai"[-1] = >"i" => "Hi" # out["New"] = "New"[0] = > "N" + "New"[-1] =>"w"=>"Nw" #out["Good"] = "Good"[0] => "G" + "Good"[-1] =>"d" =>"Gd" #out["Py"] = "Py"[0] + "Py"[-1] => "Py"
#     i+=1 # 0=>1=>2 => 3 => 4 => 5
# print(out)

# i/p = > "hai hello"
# o/p = > "olleh iah"

# s = "hai hello".split() # ["hai","hello"]
# i=0
# out=''
# while i<len(s):
#     out = s[i][::-1]+' '+ out 
#     i+=1
# print(out)
# s = "hai hello"
# print(s[::-1])

#  wap to print odd or even in a single line without using if conditions and looping
# by using list and indexing

# print(["Even","Odd"][0])
# print(["Even","Odd"][int(input("Enter Number : "))%2]) #25%2 => 1

#  i/p
# i=0
# while
# s1[0] = > 1 , s1[0] = 1 != => s1[i] != s2[i] if true increase count
# o/p : count = 2
# s1 = "111000"
# s2 = "110010"
# count = 0
# i=0
# while i<len(s1):
#     if s1[i] !=s2[i]:
#         count+=1
#     i+=1

# n = 5
# n 1 : Enter number :
# n 2 : Enter number :
# n 3 : Enter number : 
# n 4 : Enter number :
# n 5 : Enter number :
# find sum of all numbers
# then later find average of numbers
# n = int(input("Enter Number : "))
# i=1
# sum = 0
# while i<=n:
#     num = int(input(f"n {i} : Enter NUmber : "))
#     sum+=num
#     i+=1
# print(f"The sum of numbers is {sum} and average is {sum/n}")
# wap to convert binary to decimal number
# 1001
n = int(input("Enter number : "))
sum =0
p=0
while n!=0:
    lastdigit = n%10
    sum+= lastdigit*2**p
    p+=1
    n//=10 # or n=n//10
print(sum)
    
# wap to convert decimal to binary
# i/p : 9
# o/p: # 1001






# n= 9
# s=""
# start while loop n!=0 #9!=0 true 4!=0 true # 2!=0 true #1!=0 true # 0!=0 false
# rem = n%2 # 9%2 = > 1 # 4%2 => 0 # 2%2 = > 0  # 1%2 = > 1
# add that rem value to string that is 's' , add again to string 's'
#again should add rem to string , again should add rem to 's'
# n//=2 # 9//2 => #4 # 4//2 = > 2 #2//2 => 1 # 1//2 => 0

# wap to find gcd of 2 number
# Greatest common divisor
# n1 = 10 - 1,2,5,10
# n2 = 20 - 1,2,4,5,10,20
# common divisors - 1,2,5,10 => 10
# 10%1==0 ,10%2==0,.......,10%10==0 # 10
# 20%1==0,.....................,20%20==0 #20
# i = 1
# endvalue = min(n1,n2) =>min(10,20) = > 10 # endvalue = 10
# gcd = 0 # 1 #2
# while i<=endvalue:  1,2,3,4,5,6,7,8,9,10
# check condition n1%i ==0 and n2%i ==0 # 10%1 ==0 true and 20%1==0 true
# 10%2==0 and 20%2==0 true, 10%3==0 and 20%3==0 # false
# gcd = i # 1 #2
# i+=1
# n1 = int(input("Enter number 1 : ")) #10
# n2 = int(input("Enter number 2 : ")) #20
# i=1
# endvalue = min(n1,n2) # find minimum of two numbers
# gcd = 0 # 1 # 2 # 5 # 10
# while i<=endvalue: # 1<=10 #2<=10 #3 # 4 # 5 #10
#     if n1%i==0 and n2%i==0: # we are checking the both numbers are divisible by divisor or not if both are divisible then # 10%1==0 and 20%1==0 # true #10%2==0 and 20%2==0 true
#         gcd = i # update divisor to gcd 
#     # print(i)
#     i+=1 # updation
# print(f"The GCD of {n1} and {n2} is GCD : {gcd}")

# wap to find lcm of 2 number 
# least common multiple
# 10 - 10,20,30,40,50,60,70,80,90,..................
# 15 - 15,30,45,60,75,90,...........................
# common multiple numbers = > 30,60,90
# o/p : 30
# max(10,15) # 15
# 15%10 ==0 and 15%15==0 # 30%10==0 and 30%15==0 # true
# lcm = val
# break
# val = max(n1,n2) => 15
# max_val = val
# val+=val = > 15+15 => 30+30 = > 60 # wrong 
# val+=max_val 15+15 => 30+15 => 45
 
# n1 = int(input("Enter number 1 : ")) #10
# n2 = int(input("Enter number 2 : ")) #15
# max_value = max(n1,n2)
# upt_value = max_value # 15
# lcm = 0
# while True:
#     if max_value%n1==0 and max_value%n2==0:
#         lcm=max_value
#         break
#     max_value+=upt_value
# print(lcm)
