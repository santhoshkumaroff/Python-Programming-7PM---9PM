# elif
# n = int(input("Enter option "))
# if n==1:
#     print("IronMan")
# elif n==2:
#     print("Batman")
# else:
#     print("Invalid Option")
#factorial 
def fact(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
    return fact

#strong number
def strong(n):
    sum=0 #0+1 => 1
    for i in str(n): #1 0
        sum+=fact(int(i))
    return n==sum
#perfect number
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n
#amstron number
def amstrong(n): #150
    sum=0
    for i in str(n):
        sum+=int(i)**len(str(n))
    return n==sum
#prime number
def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
# match case
# option = int(input("Enter Option"))
# match option:
#     case 1:
#         print("IronMan")
#     case 2:
#         print("Batman")
#     case _: # case default
#         print("Invalid")
        
# option 
# 1 - Perfect or not
# 2 - amstrong number
# 3 - factorial
# 4 - strong number
# 5 - prime or not
# Invalid Option

def numberslogic():
        option = int(input("Enter Option .. "))
        match option:
            case 1:
                print(perfect(int(input("Enter Number : "))))
            case 2:
                print(amstrong(int(input("Enter Number : "))))
            case 3:
                print(fact(int(input("Enter Number : "))))
            case 4:
                print(strong(int(input("Enter Number : "))))
            case 5:
                print(prime(int(input("Enter NUmber : "))))
            case _:
                print("Invalid Option")
                numberslogic()
numberslogic()
# def abc():
#     print("perfect")
# print(abc())

# balance =10000
# 1 check balance # 
# 2 withdraw # withdrawal amount <balance:
# show balance
# 3 deposit #add amount to balance
# display balance