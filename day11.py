# wap to check the given number is prime or not.
# n = int(input("Enter number : "))
# l = []
# for i in range(1,n+1):
#     if n%i==0:
#         l+=[i]
# if len(l)==2:
#     print("Prime number")
# else:
#     print("Not a Prime number")

# 1 - TSB 2- if cond 3- else 4- FSB
# print("Prime number") if len(l)==2 else print("Not a Prime number")

# method 2

# n = int(input("Enter number : "))
# count = 0
# for i in range(2,n//2):
#     if n%i==0:
#         count=1
# # if count==0 and n!=1:
# #     print("Prime number")
# # else:
# #     print("not a Prime number")
# print("Prime number") if (count==0 and n!=1) else print("not a Prime number")

# wap to find the factorial of given number.

# n = 5 # 5*4*3*2*1
# fact =1
# for i in range(n,0,-1): #1*2*3*4*5 # for i in range(n,0,-1):
#     fact*=i
# print(fact)

# strong number 
# 148 = 1!+4!+8!
num=145
# sum =0
# for n in str(num):
#     # print(n,type(n)) # '1'
#     fact =1
#     for i in range(int(n),0,-1):
#         fact*=i # fact = fact*i
#     sum+=fact # sum=sum+fact
# print(sum)

# num=int(input("Enter number : ")) 
# sum=0 
# for n in str(num): 
#     fact = 1 
#     for i in range(1,int(n)+1): 
#         fact*=i 
#     sum+=fact 
# print(sum==num) 
# print('strong number') if sum==num else print("not strong number")

# wap to check the given number is amstrong number or not.
# n = 167 #1**3+6**3+7**3
# l=len(str(n)) # 3
# sum=0 #1
# for n in str(n)
#    sum+=int(n)**l #0+1**3 => 1+6**3 = >+7**3=sum
#given number == sum #print("amstrong number")

# num=153
# sum=0
# l=len(str(num))
# print("before n ",num)
# for n in str(num):
#     print("inside",n)
#     sum+=int(n)**l
#     # print(sum)
# print("outside",num,n,sum)
# if n == sum:
#     print("Amstrong")
# else:
#     print("Not amstrong")

