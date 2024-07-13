#wap to check the given number is perfect or not.
# n = 6 #1,2,3 = > 1+2+3 = > 6
n=6
sum=0
# for i in range(1,n):
#     if n%i==0:
#         sum+=i
# print(sum)
# for i in range(1,(n//2)+1):
#     if n%i==0:
#         sum+=i
# print(sum)

# wap to find hcf of two number
# n1 = 10 - 1,2,5,10
# n2 = 15 - 1,2,3,5,15
# n1 =10
# n2 = 15
# hcf = 0 #1 #2 #5
# for i in range(1,min(n1,n2)+1):
#     if n1%i==0 and n2%i==0:
#         hcf = i
# print(hcf)


# wap to convert binary to decimal values.
# 1101 = >13
# n =1101 #1111
# sum =0
# p=0
# for i in str(n)[::-1]: #"1101" #'1'
#     sum+=int(i)*2**p #'1'=> 1
#     p+=1
# print(sum)

# wap to convert decimal to binary
# n=13
# n=13
# out =''
# for i in range(n): #0
#     if n==0:
#         break
#     else:
#         rem = n%2 #13%2 ==> 1 #6%2=>0 3%2 =>1 #1%2=>1
#         out = str(rem) + out # 1=>'1' +''=>'1' #0=>'0'+'1' => '01' #1 => '1' +'01' => '101' # 1>'1'+'101' =>'1101'
#         n//=2 #13//2 => 6 //2 => 3//2 =>1//2 =>
# print(out)

# wap to find super digit of a given
# n = 5681247 =>5+6+8+1+2+4+7 = >sum= 33=>n=sum = >3+3 =>6
# while check the given number length not equal to 1
# find sum of all number 
# assign sum value to n
n=5681247 # 33 
while len(str(n))!=1: #len("5681247")!=1 7!=1 # 2!=1 #1!=1
    sum =0 #33 #0 #6
    for i in str(n): #"5681247" #"33"
        sum+= int(i) # 0+5=>5+6=>11+8=>19+1=>20+2=>22+4=>26+7=>33 ### 0+3=>3+3=>6
    print(n,sum)
    n=sum #n=33 #n=6