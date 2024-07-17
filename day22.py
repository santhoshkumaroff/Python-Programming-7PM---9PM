'''
Lcm = n1*n2/hcf

'''
# n1=int(input("Enter n1 : "))
# n2=int(input("Enter n2 : "))
# hcf=0
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         hcf=i
# print(f"Lcm of {n1} and {n2} ==> {n1*n2//hcf}")

# def lcm(n1,n2):
#     hcf=0
#     for i in range(1,min(n1,n2)+1):
#         if n1%i==0 and n2%i==0:
#             hcf=i
#     return n1*n2//hcf
# n1=int(input("Enter n1 : "))
# n2=int(input("Enter n2 : "))
# print(f"Lcm of {n1} and {n2} is {lcm(n1,n2)}")

#5! => 5*4*3*2*1 => 120
# def fact(n):
#     fact=1
#     for i in range(n,0,-1):
#         fact*=i
#     return fact
# print(fact(5))

def fact(n): #0
    print("H")
    if n==0: #1==1 #0==1
        return 0
    elif n==1:
        return 1
    return n*fact(n-1)
# print(fact(10))

def strong(n):
    sum=0 #0+1 => 1
    for i in str(n): #1 0
        sum+=fact(int(i))
    return n==sum
print(strong(10))
'''
step 1 :
def fact(5):
    if 5==1:
        return 1
    return 5*fact(4) ==> 5*24 => 120
step 2 :
def fact(4):
    if 4==1:
        return 1
    return 4*fact(3) ==> 4*6=> 24
step 3 : 
def fact(3):
    if 3==1:
        return 1
    return 3*fact(2) => 3*2 => 6
step 4 :
def fact(2):
    if 2==1:
        return 1
    return 2*fact(1) ==> 2
step 5 :

def fact(1):
    if 1==1:
        return 1
    return 1*fact(0) => 1*1
step 6:
def fact(0):
    if 0==0:
        return 1
step 6 :
fact(1)==>1
    
step 4 :   return 2*1 = > 2
fact(2) => 2
fact(3) ==> 6
fact(4) ==> 24
fact(5) ==> 120
'''
'''
fact(6)
'''
'''
145 = > 1!+4!+5!
'''