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