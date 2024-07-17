#1
# def name1():
#     a=10
#     print(a)
# b=name1()
# print(b)
# 10 
# None

# 2
# def name2():
#     a=10
#     return a
# # name2()
# # b= name2()
# # print(b)
# print(name2())
# # 10

# wap to check odd or even
# def odd_even(n):
#     if n&1==0:
#         print("Even")
#     else:
#         print("ODD")
# def odd_even(n):# odd_even(0)
#     if n&1!=0: #15 is even or not
#         return True
#     return False
# print(odd_even(7))

# wap to print even numbers between the range:
# for i in range(0,10): #0 #1
#     if odd_even(i): #odd_even(0) # if True #odd_even(1) #if False
#         print(i,end=" ")
#0

# wap to check the given number is prime or not by using function

# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             print("Not a prime")
#             break
#     else:
#         print("Prime")       
# prime(6)

# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# for i in range(0,20):
#     if prime(i) and i>=2:
#         print(i,end=" ")

# def amstrong(n):
#     sum=0
#     for i in str(n):
#         sum+=int(i)**len(str(n))
#     return sum==n
# print(amstrong(153))

# def perfect_number(n,sum=0):
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     return sum==n
# print(perfect_number(218))
def fact(n,fact=1):
    # if n<=1:
    #     return True
    # return n*fact(n-1)
    for i in range(n,0,-1):
        fact*=i
    return fact

def strongnumbers(n,sum=0):
    for i in str(n):
        fact=1
        for j in range(int(i),0,-1):
            fact*=j
        sum+=fact
    return sum==n
# print(strongnumbers(145))