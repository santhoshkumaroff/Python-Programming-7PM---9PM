'''

*
*
*
*
*
n=5
  0
0 * * * * *
1 *
2 * * * * *1
3         *1
4 * * * * *1
1) i==0
2) i==n//2
3) i == n-1
4) j==0 and i<=n//2 ###(j==0 and 0<=2)
5) j==n-1 and i>=n//2
'''
# n=7
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n//2 or i==n-1 or (j==0 and i<=n//2) or (j==n-1 and i>=n//2):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
'''
n=5
  
0|        * ->4space
1|      * * * -> 3 space
2|    * * * * * -> 2 space
3|  * * * * * * * -> 1space
4|* * * * * * * * *

one loop is for row
two loop for only columns 
1) space (n-i-1) 0=> 5-0-1=>4 , 1=> 5-1-1=>3, 2=>5-2-1 => 2 ,3 => 5-3-1 => 1,4 => 5-4-1=>0,0
2) star ->0==> 2*i+1 (2*0+1)=>1 ==> * , 1 (2*1+1)==> * * *, 2 (2*2+1)==>5 , * * * * * ,3 => (2*3+1)=>7 ==> 7 stars => 4 (2*4+1) ==> 9 stars

__ __ __ __ *              --> 1
__ __ __ *  *  *           --> 3 
__ __ *  *  *  *  *        --> 5 
__ *  *  *  *  *  *  *     --> 7
*  *  *  *  *  *  *  *  *  --> 9

3 lines
'''
n=5
for row in range(n): #0 #1 #2 #3 #4
    for space in range(n-row-1): #4 #5-1-1=>3 #2 =>5-2-1 =>2 #1 #5-4-1=>0
        print(" ",end= " ")
    for star in range(2*row+1): # 1 #2*1+1 ==>3 #2*2+1=>5 #7 #2*4+1 => 9
        print("*",end=" ")
    print()
'''
__ __ __ __   *
__ __ __ __ * * *
__ __    *  * * * *
__    *  *  * * * * *
*     *  *  * * * * * *

'''
'''
  1
 123
1234
12345
1234567
123456789
'''
# n=5
# for row in range(n): 
#     val=1   
#     for space in range(n-row-1): 
#         print(" ",end= " ")
#     for star in range(2*row+1):
#         print(val,end=" ")
#         val+=1
#     print()
'''
        *
      * 0 *
    * 0 * 0 *
  * 0 * 0 * 0 *
* 0 * 0 * 0 * 0 *

        *
      *   *
    *   *   *
  *   *   *   *
*   *   *   *   *

'''
'''
1) In a 3 lines should solve
        * 
      * * * 
    * * * * * 
  * * * * * * * 
* * * * * * * * * 

2) Reverse pyramid
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 

3) 
*   *   *   *   *
  *   *   *   *
    *   *   *
      *   *
        *
'''