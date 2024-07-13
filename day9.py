# i/p = ["Hai","Hello","Good"]
# o/p = > {"Hai":3,"Hello":5,"Good":4}
# l = ["Hai","Hello","Good"]
# i = 0
# out ={}
# while i<len(l): # 0 # 1 #2
#     out[l[i]]=len(l[i]) # out['Hai'] = 3 # out[l[1]]=> out["Hello"] = 5 = > out[l[i]] = > out["Good"] = 4
#     i+=1
# print(out)

# i/p : l = ["Hai",20,46.7,"New","Good","Py"]
# o/p : {"Hai":"Hi","New":"Nw","Good":"Gd","Py":"Py"}

# i = 0
# out = {}
# type of value which is equal to str
# add it to out key is "Hai" and value = l[i][0] + l[i][-1]
# i+=1
# print out
# l = ["Hai",20,46.7,"New","Good","Py"]
# i=0
# out ={}
# while i<len(l): # 0 # 1 #2 # 3 #4 #5
#     if type(l[i]) == str: #l[0] => "Hai" == str # yes it is string type(20) == str # type(46.7) == str #New => type("New")==str
#         out[l[i]] = l[i][0] + l[i][-1] # => out["Hai"] = "Hai"[0] => "H" + "Hai"[-1] = >"i" => "Hi" # out["New"] = "New"[0] = > "N" + "New"[-1] =>"w"=>"Nw" #out["Good"] = "Good"[0] => "G" + "Good"[-1] =>"d" =>"Gd" #out["Py"] = "Py"[0] + "Py"[-1] => "Py"
#     i+=1 # 0=>1=>2 => 3 => 4 => 5
# print(out)

# i/p = > "hai hello"
# o/p = > "olleh iah"

# s = "hai hello".split() # ["hai","hello"]
# i=0
# out=''
# while i<len(s):
#     out = s[i][::-1]+' '+ out 
#     i+=1
# print(out)
# s = "hai hello"
# print(s[::-1])

#  wap to print odd or even in a single line without using if conditions and looping
# by using list and indexing

# print(["Even","Odd"][0])
# print(["Even","Odd"][int(input("Enter Number : "))%2]) #25%2 => 1

#  i/p
# i=0
# while
# s1[0] = > 1 , s1[0] = 1 != => s1[i] != s2[i] if true increase count
# o/p : count = 2
# s1 = "111000"
# s2 = "110010"
# count = 0
# i=0
# while i<len(s1):
#     if s1[i] !=s2[i]:
#         count+=1
#     i+=1

# n = 5
# n 1 : Enter number :
# n 2 : Enter number :
# n 3 : Enter number : 
# n 4 : Enter number :
# n 5 : Enter number :
# find sum of all numbers
# then later find average of numbers
# n = int(input("Enter Number : "))
# i=1
# sum = 0
# while i<=n:
#     num = int(input(f"n {i} : Enter NUmber : "))
#     sum+=num
#     i+=1
# print(f"The sum of numbers is {sum} and average is {sum/n}")
# wap to convert binary to decimal number
# 1001
n = int(input("Enter number : "))
sum =0
p=0
while n!=0:
    lastdigit = n%10
    sum+= lastdigit*2**p
    p+=1
    n//=10 # or n=n//10
print(sum)
    