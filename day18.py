'''
n=4

*  1  2  3
1  *  1  2
1  2  *  1
1  2  3  *

# we should take third variable
# left to right diagonal ==> i==j then print *
# else print numbers
'''

# n=5
# for i in range(n):
#     val=1
#     for j in range(n):
#         if i==j:
#             #val=1
#             print("*",end=" ")
#             val=1
#         else:
#             print(val,end=" ")
#             val+=1
#     print()


'''

      Z
    Z Y
  Z Y X
Z Y X W
'''
# n=5
# for i in range(n):
#     val = ord('Z')
#     for j in range(n):
#        if i+j>=n-1:
#            print(chr(val),end=" ")
#            val-=1
#        else:
#            print(" ",end=" ")
#     print()
            
'''
Z Y X W 
Z Y X W 
Z Y X W 
Z Y X W 

n=4
      W
    X W
  Y X W
Z Y X W 
'''
n=4
# for i in range(n):
#     val = ord('Z')
#     for j in range(n):
#         print(chr(val),end=" ")
#         val-=1
#     print()

# for i in range(n): #0 1 2 3
#     val = ord('Z') #90 #89 #88 #87 #90 #89 #88 #87
#     for j in range(n): #0
#        if i+j>=n-1:
#            print(chr(val),end=" ")
#        else:
#            print(" ",end=" ")
#        val-=1
#     print()
# print(ord('Z'))
'''

     0  1  2  3
0 ->          W
1 ->       X  W
2 ->      


'''

'''
n=5
       0  1   2  3  4

-> 0  1*  *  *  2*
-> 1  1*        2*
-> 2  1*        2*
-> 3  1*  *  *  2*
-> 4              *


j==n-2 and i<=n-2
j==0 and i<=n-2
i==n-2 and j<=n-2
3 and 0<=3 -->
3 and 1<=3 -->
3 and 2<=3 -->
i==n-1 and j==n-1 or
        *
        *
        *
        *
*  *  * *<---

i==0 and j<=n-2
0==0 and 0<=3
0 and 1<=3
0 and 2<=3
0  and 3<=3
0 and 4<=3



1) i==n-1 and j==n-1
2) i==0 and j<=n-2
3) 
'''
# n=7
# for i in range(n):
#     for j in range(n):
#         if (i==n-1 and j==n-1) or (i==0 and j<=n-2) or (i==n-2 and j<=n-2) or (j==0 and i<=n-2) or (j==n-2 and i<=n-2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''


13*         *2
1*  3*   *  *2
1*    3*    *2
1*          *2
1*          *2

i==j and 
j==0 or 1 
j==n-1
'''


# for i in range(n):
#   for j in range(n):
#     if j==0 or j==n-1 or (i==j and j<=n//2) or (i+j==n-1 and j>=n//2):
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()