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

'''For loop'''

# wap to check whether the given list is homogeneous or heterogeneous.
l=[5,8,6,'Hai']
# for i in l
# type(l[0]) != type(i)
# print("Heterogeneous")
for i in l:
    if type(l[0]) != type(i):
        print("Heterogeneous")
        break
else:
    print("Homogeneous")

# for i in range(len(l)):
#     if type(l[0]) != type(l[i])

# wap to remove duplicate values from list without using inbuild function.

# 
l=['apple',5,8,6,6] #'apple'
out=[] #'apple' #5 #8 #6 #6
for i in l: #'apple'
  if i not in out:
      out+=[i]
print(out)

# wap to split the string without using split function
s = "   Cricket    Football   "
# print(s)
# temp='' 'Cricket' # empty temp string
# out = [] #['Cricket']
# fetch values from string  
# check the values is having empty " "
# if it is not having empty space 
# just add string to temp variable
# if you have empty space just add temp string to given list
# 
temp=""
out = []
for i in s:
    if i!=" ":
        temp+=i
    else:
        out+=[temp]
        temp=""
else:
    out+=[temp]
# print(out)
out = ['', '', '', 'Cricket', '', '', '', 'Football', '', '', '']
res = [] #'Cricket' 'Football'
for i in out:
    if i!= "": #''!=''
        res.append(i)
        
print(res)

# s=" hello world "
# s_='' 
# l=[] 
# for ch in s: 
#     if ch != " ": 
#         s_+=ch 
#     else: 
#         l.append(s_) 
#         s_='' 
# else: l.append(s_) 
# print(l) 
# l2=[] 
# for word in l: 
#     if word != "": 
#         l2.append(word) 
# print(l2) 