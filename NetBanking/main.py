# import packages
import sqlite3
import random

conn = sqlite3.connect('mydb.db')

# data = list(conn.execute('''select * from SBI_IFSC where ifsc_code = "SBIN0021874" '''))
# print(data)
# print(data[0][2])

# data = list(conn.execute('''select  BRANCH_NAME from SBI_IFSC where CITY_NAME = "BANGALORE"'''))
# print(data)
'''
1. HSR LAYOUT RD SECTOR
2. WHITEFIELD - BANGALORE
3. HBR LAYOUT
4. UTTARAHALLI
5. VASANTH NAGAR - BANGALORE
6. J P NAGAR EIGHT PHASE
'''
# listofbranches = [i[0] for i in data]
# for i in range(1,len(listofbranches)+1):
#     print(f'{i}. {listofbranches[i-1]}')
# print(list(zip("Hi","Hi")))

#modify ...
# amount =5000
# conn.execute(f'''update AccountDetails set bank_balance ="{amount}" where username ="nadim@gmail.com"''')
# conn.commit()


#showProfile
def showprofile(userdetails):
    # print(userdetails)
    print("Profile Details 👇👇👇")
    print("----------------------------")
    print(f"Name : {userdetails[-1]} \nUsername : {userdetails[1]}\nAccount no : {userdetails[-3]}\nIFSC CODE : {userdetails[-5]}\nBank Name : {userdetails[4]}\nBranch Name : {userdetails[3]}")
    while True:
        option = int(input("Enter 1 for back to show features : "))
        if option==1:
            showfeatures(userdetails)
            break
        else:
            print("Invalid Option..")
        


#showfeatures 
def showfeatures(userdetails):
    print("1. Net Banking\n2. Show Profile\n3. Deposit\n4. Check Balance\n5. Exit")
    option = int(input("Enter Correct Option : "))
    match option:
        case 1:
            print("NetBanking")
        case 2:
            # print("Show Profile")
            showprofile(userdetails)
        case 3:
            print("Deposit")
        case 4:
            print("Check Balance")
        case 5:
            return 0
        case _:
            print("Invalid Option ❌❌❌")
            showfeatures()
#check user password
def checkuserpassword(username):
    print(f'Username : {username}')
    user_db_pass = list(conn.execute(f'''select password from AccountDetails  where username ="{username}"'''))[0][0]
    user_pass = input("Enter Password : ")
    if user_pass == user_db_pass:
        print("Login Successful ✅✅✅")
        userdetails = list(conn.execute(f'''select * from AccountDetails where username ="{username}"'''))
        userdetails = [i for i in userdetails[0]]
        showfeatures(userdetails)
    else:
        print("Incorrect Password")
        checkuserpassword(username)

#login starts here
def loginunsernamecheck():
    # print("Login Success ")
    user_name = input("Enter User name : ")
    allusername = list(conn.execute('''select username from AccountDetails '''))
    allusername = [i[0] for i in allusername]
    #  in 
    if user_name.endswith("@gmail.com"):
        if user_name in allusername:
            print("Username Matching ✅✅✅")
            checkuserpassword(user_name)
        else:
            print("Username Incorrect ❌❌❌")
            loginunsernamecheck()
    else:
        print("Invalid Username")
        loginunsernamecheck()
#register starts here
def register():
    print("Register ....")

#start logic here

def start():
    option = int(input("1. Login \n2. Register \n3. Exit \nEnter your option : "))
    match option:
        case 1:
            print("Login Here")
            loginunsernamecheck()
        case 2:
            print("Register Here")
            register()
        case 3:
            return 0
        case _:
            print("Invalid Option ❌❌❌ ")
            start()
start()
# windowicon + .