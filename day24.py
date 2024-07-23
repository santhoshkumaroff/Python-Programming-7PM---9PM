'''
Decorator functions
'''
'''
Miscellaneous function
'''
'''
#declare the function 
def sound(text):
    return text.lower()
#calling the function
print(sound("Saturday")) 
# it used to store function id to obj then next obj will perform like that stored function
abc = sound # this has some function id store it to obj,now obj is perform all the operation like sound func

print(abc("No holiday"))
'''
'''
starts from line number 11 --> 8 line declaration part --> 9th line will return values -->11 print text -->13--> 15 --->8-->9th print text 
'''
'''
Passing function as a argument
'''
#declaring the functions
def one(text):
    return text.lower() #today is saturday

def two(text):
    return text.upper() # Today is Saturday

def printmsg(func): #func = one function id # func = two
    print(func("Today is Saturday")) # one("Today is Saturday") # two("Today is Saturday")
     #today is saturday
    
# printmsg(one) #passing function as a argument
# printmsg(two)
'''
starts from 35 --> 31 --> 32 --> 25 --> 26-->32-->33 -->36 -->31-->32-->28-->29-->32
'''
'''
Example 2
'''
'''
Just adding two number
'''
# def add_func(a): #a=20
#     def add_logic(b): #15
#         return a+b #20+15==>35
#     return add_logic # 

# add_two = add_func(20) # add_two = not having any of the values the later calling the func and return some values or function id the later we should store this to variable
# print(add_two(15)) #35

'''
51 --> 46--> 49  -->51-->52-->47-->48-->
'''
'''
start decorator
'''
def start_deco(func): #func == msg
    def inner():
        print("Monday..")
        func()
        print("Tuesday")
    return inner
@start_deco # similar to msg = start_deco(msg)
def msg():
    print("Inside Function Here")
# msg = start_deco(msg) #return inner function id and stored in msg
msg()

def add(a,b):
    return a+b
print(add(10,20))

'''
start-69-->60-->65-->69-->70-->61-->62-->63-->67-->68-->64-->end
'''