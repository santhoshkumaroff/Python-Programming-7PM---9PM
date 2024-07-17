# wap to check the given number is amstrong or not by using functions.
# 153 =>1**3+5**3+3**3
def amstrong(n): #150
    sum=0
    for i in str(n):
        sum+=int(i)**len(str(n))
    return n==sum
# print(amstrong(150))
# def rangeamstrongnum(start,end):
#     for i in range(start,end):
#         if amstrong(i):
#             print(i,end=" ")
# rangeamstrongnum(0,1000)
# for i in range(0,1000):
#         if amstrong(i):
#             print(i,end=" ")
            
#6 = 1,2,3 =>1+2+3=6
#
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    # if sum==n:
    #     return True
    # return False
    return sum==n
# perfect(27)
# for i in range(1,1000):
#     if perfect(i):
#         print(i,end=" ")

print(*[i for i in range(1,1000) if perfect(i)])
#[val for loop if cond]
# l = [val for val in range(1,11) if val%2!=0]
# l=[]
# for i in range(1,11):
#     if i%2==0:
#         l.append(i)
#1) It is used to reduce the number of instruction(lines of code)
#2) It is used to compress the looping and conditional statement finally it will return values in the form of list
# print(*l)
# for i in l:
#     print(i,end=" ")

# wap to convert binary to decimal by using functions 
# wap to convert decimal to binary by using functions