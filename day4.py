# wap to find the length of the given data only if it is list before should whether the data is Multivalue datatype or collections.

# data = eval(input())
# if type(data) in [str,list,tuple,set,dict]:
#     print(f"Yes {type(data)} is MVD or collections ")
#     if type(data) == list:
#         print(f'The length of {data} is {len(data)}')
#     else:
#         print(f'{data} type is not a list')
# else:
#     print(f"{data} is not MVD or collections")

# wap to find the greatest of two number.
# wap to find the greatest of three number.
# num1 = int(input("Enter number 1"))
# num2 = int(input("Enter number 2"))
# num3 = int(input("Enter number 3"))
# if num1>num2 and num1>num3:
#     print(f'{num1} is greater than {num2} and {num3}')
# elif num2>num3:
#     print(f'{num2} is greater than {num1} and {num3}')
# else:
#     print(f'{num3} is greater than {num1} and {num2}')

# wap to find the second greatest among three numbers

num1 = int(input("Enter num 1"))
num2 = int(input("Enter num 2"))
num3 = int(input("Enter num 3"))
if num1>num2 and num1>num3:
    print(f"{num1} is greater")
    if num2>num3:
        print(f"{num2} is second greatest")
    else:
        print(f"{num3} is second greatest")
elif num2>num3:
    print(f"{num2} is greater")
    if num1>num3:
        print(f"{num1} is second greatest")
    else:
        print(f'{num3} is second greatest')
else:
    print(f"{num3} is greater")
    if num1>num2:
        print(f"{num1} is second greatest")
    else:
        print(f"{num2} is second greatest")
        
# wap to find the second greatest among four numbers(assignment)
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# if num1>num2 and num1>num3 and num1>num4:
#     print(f"{num1} is greater")
#     if num2>num3 and num2>num4:
#         print(f"{num2} is second greatest")
#     elif num3>num4:
#         print(f"{num3} is second greater")
#     else:
#         print(f"{num4} is second greater")


# wap to check whether the char is uppercase,lowercase,digit or special char

#wap to check whether the given integer is 1 digit ,2 digit,3 digit,more than 3.

#wap to check given points are lying in which quadrant.
# take 2 numbers(assignment)
# both numbers are + - 1st quadrant 
# one positive,one negative - 2 quadrant
# both negative - 3 quadrant
# one negative , one postive - 4th quadrant

num1 = int(input())
num2 = int(input())
if num1>0 and num2>0:
    print("1st Quadrant")
elif num1>0 and num2<0:
    print("2nd Quadrant")
elif num1<0 and num2<0:
    print("3rd Quadrant")
else:
    if num1==0 and num2 ==0:
        print("Zero Invalid")
    else:
        print("4th Quadrant")