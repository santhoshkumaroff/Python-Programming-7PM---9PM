# # 1
# num = int(input())
# if num|1 == num+1:
#     print("even")
    
# # wap to check whether a list consists of middle value or not.

# l1 = [1,2,3,4]
# l2=[1,2,3,4,5]
# if len(l2)%2==0:
#     print("No")
# else:
#     print(f"Yes {l2} mid value is {l2[len(l2)//2]}")


#wap to check whether two values are pointing to the same address


# consider a tuple of length 2 and check tuple is homogenous or heterogenous.
# tuple1 = (1,"hi")
# t1 = tuple(input())
t1 = (1,"hi")
print(t1,type(t1))

# Take one input from user list or tuple and remove duplicate values in a single line

# wap to check whether the number is positive or negative.


'''nested if'''
# 1) wap to login into instagram with valid username and password (enter password only if username is valid)
username = 'abcd'
password = 'abcd@123'
u_username = input()
if u_username == username:
    u_pass = input()
    if u_pass == password:
        print("Login")
    else:
        print("Password miss match")
else:
    print("Invalid username")
    
# 2) wap to print the middle value of a list only if it is a string

l1 = [1,2,3,4,"yes",0,9,8,7]
if len(l1)%2 !=0:
    if type(l1[len(l1)//2]) == str:
        print("the middle value is",l1[len(l1)//2])
    else:
        print('not a string')
else:
    print("not having middle value")
    
    
# 3) wap to check whether char is vowel or consonent ,not an alphabet.

char = input()
if 'A'<=char<='Z' or 'a'<=char<='z':
    if char in 'aeiouAEIOU':
        print(f'Yes {char} is vowel')
    else:
        print("consonant")
else:
    print("Not an alphabet")