'''
n=5
 0 1 2 3 4 
0         * -->(0,4) = 4 = i+j
1       *   -->(1,3) = 4
2     *     -->(2,2) = 4
3   *       -->(3,1) = 4
4 *         -->(4,0) = 4

i+j == n-1
n=5
  1 2 3 4 5
1         * -->(1,5) = 6 = i+j
2       *   -->(2,4) = 6
3     *     -->(3,3) = 6
4   *       -->(4,2) = 6
5 *         -->(5,1) = 6
i+j == n+1
'''
# n=5
# for i in range(n):
#     for j in range(n):
#        if  i+j == n-1:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#        if  i+j == n+1:
#            print("*",end=" ")
#        else:
#            print(" ",end=" ")
#     print()

'''
n=5
          1
        *  
      2    
    *      
  3      
# '''
# n=5
# v=1
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             if i%2==0:
#                 print(v,end=" ")
#                 v+=1
#             else:
#                 print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

'''
n = 5- 0 1 2 3 4
v = n//2
          C --> chr(65+2)
        *  
      B    
    *      
  A 
   
n = 7
              D
            *
          C
        *  
      B    
    *      
  A 
'''
n=9
# v=n//2
# for i in range(n):
#     for j in range(n):
#         if i+j==n-1:
#             if i%2==0:
#                 print(chr(65+v),end=" ")
#                 v-=1
#             else:
#                 print("*",end=" ")
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
'''
# n=5
# for i in range(n):
#     for j in range(n):
#         if i+j>=n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
