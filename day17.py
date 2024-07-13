'''
row
0          *
1
2      * * *
3
4  * * * * *
'''
# n=8
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             if i%2==0:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''
     col
   0 1 2 3 4
0          *
1        1 *
2      * 2 *
3    3 * 4 *
4  * 5 * 6 *

# stars are present in even columns
# i+j==n-1
# i+j>n-1
'''
# n=5
# val=1
# for i in range(n): #0 
#     for j in range(n): #0 #1 #2 #3 #4
#         if i+j>=n-1: #0+0==5-1 ==>0==4 0+1 =1 ==4
#             if j%2!=0: #4 #3
#                 print(val,end=" ")
#                 val+=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
'''
  1 2 3 4 5
1 *
2 * *
3 * * *
4 * * * *
5 * * * * *

i>=j
'''
'''
*
  *
    *
      *
        *
'''

'''
i<=j
  0 1 2 3 4
0 * * * * *
1   * * * *
2     * * *
3       * *
4         *


'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()






'''
n=5
  0 1 2 3 4
0         * -->1) i+j==n-1 
1       * * -->2) i+j==n-1 ,i+j>n-1 5>4 lhs : i+j =>(1,5)=>5 rhs : n-1 => 5-1 = 4 => 5>4
2     * * * -->3) i+j==n-1, lhs : i+j => (2,3)=> 5 : n-1 =>4 5>4,lhs : ()
3   * * * *
4 * * * * *
i+j>=n-1
'''
'''
* * * * *
* * * * 
* * *
* *
*
i+j<=n-1
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j<=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''
*
  *
    * 
      * 
        *
        i==j
'''
'''

        *
      *
    *
  *
*
i+j==n-1
'''
'''
*       *
  *   *
    * 
  *   * 
*       *
'''
'''
n=5
* * * * *





'''

'''
n=5
0
1
2
3
4 * * * * * n-1

'''

# n=5
# for i in range(n):
#     for j in range(n):
#         if i==0:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
# n=5
# for i in range(n):
#     for j in range(n):
#         if i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
'''
n=5

* * * * *



* * * * *
'''

'''
n=5
0 1 2 3  4
*        *
*        *
*        *
*        *
*        *
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
    
'''
* * * *  *
*        *
*        *
*        *
*        *
* * * *  *

'''

'''
#1)
n=5
2 2 2 2 2
1       1
1       1
1       1
1       1
2 2 2 2 2
#2)

* * * * $
        $
        $
        $
        $
# 3)
*
*
*
*
* * * * *

#4)
if you enter odd numbers
* * * * *
* *   * *
*   7   *
*  *  * *
* * * * *
#5)

*
* *
*   *
*     *
* * * * *
#6)


        *
     *  *
   *    *
 *      *
* * * * *

'''
'''
1
*  2
*     3
*        4
*  *  *  *  5
'''
# n=5
# for i in range(n):
#   for j in range(n):
#     if i==0 or i==n-1:
#       print(2,end=" ")
#     elif j==0 or j==n-1:
#       print(1,end=" ")
#     else:
#       print(" ",end=" ")
#   print()

# n=5
# for i in range(n):
#   for j in range(n):
#     if j==n-1 :
#       print("$",end=" ")
#     elif i==0:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()


'''
n=5
0
2 2 2 2 2
1       1
1       1
1       1
1       1
2 2 2 2 2
'''
# n=5
# for i in range(n+1):
#   for j in range(n):
#     if i==0 or i==n:
#       print(2,end=" ")
#     elif j==0 or j ==n-1:
#       print(1,end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
'''
* * * * $
        $
        $
        $
        $
'''

# n=5
# for i in range(n):
#   for j in range(n):
#     if j==n-1:
#       print("$",end=" ")
#     elif i==0:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
  
# n=5
# for i in range(n):
#   for j in range(n):
#     if j==0 or i==n-1:
#       print("*",end=" ")  
#     else:
#       print(" ",end=" ")
#   print()

# n=5 
# for i in range(n):
#   for j in range(n):
#     if i==n//2 and j ==n//2:
#       print("7",end=" ")
#     else:
#       print("*",end=" ")
#   print()

n=7
# for i in range(n):
#   for j in range(n):
#     if i+j==n-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()
# for i in range(n):
#   for j in range(n):
#     if i ==0 or j==0 or i==n-1 or j==n-1 or i==j or i+j==n-1:
#       if i==j and i+j==n-1:
#         print("S",end=" ")
#       else:
#         print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

# n=5
# for i in range(n):
#   for j in range(n):
#     if j==n-1 or i==n-1 or i+j==n-1:
#       print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

# n=5
# val=1
# for i in range(n):
#   for j in range(n):
#     if j==0 or i ==n-1:
#       print("*",end=" ")
#     elif i==j:
#       print(val,end=" ")
#       val+=1
#     else:
#       print(" ",end=" ")
#   print()

'''
n=5
j%2==0
pattern logic ? ==> 
values logic ? ==> j//2 ==> values
j => 2//2 ==> 1
j => 4//2 ==> 2
1) i+j ==n+1
2) i+j<n+1
combain 2 conditions => i+j<=n+1
  5 4 3 2 1
5         * --> (5,1) => 5+1 ==> 6 == 6
4       1 * --> (4,2) ==> 4+2 ==>6 ==6 , (4,1) ==> 5 < 6
3     * 1 * --> (3,3) ==> 6==6 , (3,2) ==> 5<6,(3,1) ==> 4 <6
2   2 * 1 * --> (2,4) ==> 6==6, (2,3) ==> 5<6 , (2,1) ==> 3<6
1 * 2 * 1 * --> (1,5) ==> 6==6,(1,4) ==> 5<6, (1,3)==> 4<6 ,(1,2) ==> 3<6, (1,1)==>2<6
'''
'''
* * 1 * *
* * 2 * *
1 2 3 4 5
* * 4 * *
* * 5 * *


* * 2 * *
* * 3 * *
1 2 3 4 5
* * 4 * *
* * 5 * *

A * B
  C
D * E

A B C D E
1       2
2       3
3       4
* * * * *
'''

# n=5
# for i in range(n,0,-1):
#   for j in range(n,0,-1):
#     if i+j<=n+1:
#       if j%2==0:
#         print(j//2,end= " ")
#       else:
#         print("*",end=" ")
#     else:
#       print(" ",end=" ")
#   print()

'''
* 1 2 3
1 * 1 2
1 2 * 1
1 2 3 *
'''
# n=4
# for i in range(n):
#   val=1
#   for j in range(n):
#     if i==j:
#       print("*",end=" ")
#     else:
#       print(val,end=" ")
#       val+=1
#   print()
  
'''
      1
    2 1
  3 2 1
4 3 2 1
'''
# n=4
# for i in range(n):
#   v=n
#   for j in range(n):
#     if i+j>=n-1:
#       print(v,end=" ")
#     else:
#       print(" ",end=" ")
#     v-=1
#   print()

'''
      Z
    Z Y
  Z Y X
Z Y X W
'''
# n=4
# for i in range(n):
#   v=ord('Z')
#   for j in range(n):
#     if i+j>=n-1:
#       print(chr(v),end=" ")
#       v-=1
#     else:
#       print(" ",end=" ")
#   print()
'''
      W 
    X W 
  Y X W 
Z Y X W 
'''
# n=4
# for i in range(n):
#   v=ord('Z')
#   for j in range(n):
#     if i+j>=n-1:
#       print(chr(v),end=" ")
#     else:
#       print(" ",end=" ")
#     v-=1
#   print()

# n=5
# v=2
# for i in range(n-1):
#   for j in range(n):
#     if j==n//2:
#       print(v,end=" ")
#       v+=1
#     elif i==1:
#       print(j+1,end=" ")
#     else:
#       print("*",end=" ")
#   print()
