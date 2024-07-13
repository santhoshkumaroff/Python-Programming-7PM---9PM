'''
n=5 ==> n//2 =>5//2 =>
col 0 1 2 3 4 (j)
row(i)
0   * * 1 * *
1   * * 1 * *
2   * * 1 * *
3   * * 1 * *
4   * * 1 * *

'''
#method 1
# n=5
# for i in range(n): #0 1 2 3 4
#     for j in range(n): #0 1 2 3 4
#         if j==n//2: #0 == 2,1==2,2==2
#             print("1",end=" ")
#         else:
#             print("*",end=" ")
#     print()
#method 2
'''
col   0 1 2 3 4
row
0 - > * * 1 * *
1 - > * * 1 * *
2 - > * * 1 * *
3 - > * * 1 * *
4 - > * * 1 * *
'''

# n=5 
# for i in range(1,n+1): # 1 2 3 4 5
#     for j in range(1,n+1): #
#         if j==(n//2)+1:# 5//2=> 3
#             print("1",end=" ")
#         else:
#             print("*",end=" ")
#     print()
    
'''
col  1
row
-> 1 
'''
'''
* * * * *
* * * * *
1 2 3 4 5
* * * * *
* * * * *
'''
# method 1 
# n=5
# for i in range(n):
#     for j in range(n): 0 1 2 3 4
#         if i==n//2:
#             print(j+1,end=" ")
#         else:
#             print("*",end=" ")
#     print()
# method 2
# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if i==n//2:
#             print(val,end=" ")
#             val+=1
#         else:
#             print("*",end=" ")
#     print()

'''
1)
n=5 
    *   
    *
    *
    *
    *
'''
'''
2)
n=5 



* * * * *



'''
'''
3)
     *
     *
 * * * * *
     *
     *
'''
'''
    1
    2
A B C D E
    4
    5
'''
# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if i==n//2: #1 ==2 #2==2 true 2==2 #3==2
#             print(chr(65+j),end=" ") # 2 C C C C C
#         elif j ==n//2: # 1==2 0 ==2
#             print(i,end=" ")
#             # val+=1
#         else:
#             print(" ",end=" ")
#     print()
'''
col  0 1 2 3 4
row
- >0 * * 1 * *
- >1 * * 2 * *
- >2 A B C D E
- >3 * * 3 * *
- >4 * * 4 * *
'''
'''
n =5
  1 2 3 4 5
1 * 
2   *
3     *
4       *
5         *
'''
# n=5
# val=0
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             print(chr(65+val),end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
'''triangle'''
'''
  1 2 3 4 5
1 *
2 * *
3 * * *
4 * * * *
5 * * * * *

1) i==j some of the i and j points are same
2) 2>1 3>1
i>=j
'''
'''
1
2 3
4 5 6
7 8 9 10
1 2 3 4 5
'''
# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if val>10: # val=11
#             val=1
#         if i>=j:
#             print(val,end=" ")
#             val+=1
#         else:
#             print(" ",end=" ")
#     print()
    
'''
1
* *
2 3 4
* * * *
5 6 7 8 9
'''
# n=5
# val=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             if i%2==0:
#                 print(val,end=" ")
#                 val+=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
'''
0
0 * 
0 * 0 
0 * 0 * 
0 * 0 * 0 
'''
n=5
for i in range(n):
    for j in range(n):
        if i>=j:
            if j%2==0:
                print("0",end=" ")
            else:
                print("*",end=" ")
        else:
            print(" ",end=" ")
    print()