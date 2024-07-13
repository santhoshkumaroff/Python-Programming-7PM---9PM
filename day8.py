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
import random
random_number = random.randint(1,100)
while True:
    guessing_number = int(input("Enter Number : "))
    if guessing_number>random_number:
        print(f"your {guessing_number} is greater than random number")
    elif guessing_number<random_number:
        print(f"Your {guessing_number} is smaller than random number")
    else:
        print(f'Correct the number is {random_number}')
        break
    
    
