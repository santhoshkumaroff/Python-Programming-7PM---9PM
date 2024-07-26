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

#netbanking 
def netbanking(userdetails,username):
    receiver_username = input("Enter receiver username : ")
    allusernames = list(conn.execute('''select username from AccountDetails'''))
    allusernames = [i[0] for i in allusernames]
    print(allusernames)
    if receiver_username in allusernames:
        print("Validate successful")
        while True:
            amount = int(input("Enter amount : "))
            if 0<=amount<=10000:
                print("validate")
                sender_balance = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{username}"'''))[0][0]
                receiver_balance = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{receiver_username}"'''))[0][0]    
                if amount<=sender_balance:
                    # print("Validate")
                    sender_balance-=amount
                    receiver_balance+=amount
                    conn.execute(f'''update AccountDetails set bank_balance = "{sender_balance}" where username = "{username}"''')
                    conn.commit()
                    conn.execute(f'''update AccountDetails set bank_balance = "{receiver_balance}" where username = "{receiver_username}"''')
                    conn.commit()
                    checkbalance(userdetails,username)
                    break
                else:
                    print("Not having enough balance")
            else:
                print("Invalid amount ❌❌❌")
    else:
        print("Username is not available")
        netbanking(userdetails,username)


#deposit
def deposit(userdetails,username):
    amount = int(input("Enter amount : "))
    if 0<=amount<=10000:
        print("Range valid")
        #santhosh@gmail.com
        old_balance = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{username}"'''))[0][0]
        while True:
            g_otp = random.randint(1000,9999)
            u_otp = int(input(f"OTP : {g_otp}\nEnter your OTP : "))
            if g_otp == u_otp:
                print("OTP Matching ...")
                old_balance+=amount
                conn.execute(f'''update AccountDetails set bank_balance = "{old_balance}" where username = "{username}"''')
                conn.commit()
                checkbalance(userdetails,username)
                option = int(input("Enter 1 to Back menu : "))
                while True:
                    if option ==1:
                        showfeatures(userdetails,username)
                        break
                    else:
                        print("Invalid Option")
                break
            else:
                print("Invalid OTP")
    else:
        print("Out of range ❌❌")
        deposit(userdetails,username)

#check balance
def checkbalance(userdetails,username):
    #method 1
    balance = list(conn.execute(f'''select bank_balance from AccountDetails where username = "{username}"'''))[0][0]
    print(f"Current Balance is : {balance}")
    option = int(input("Enter 1 to Back menu : "))
    while True:
        if option ==1:
            showfeatures(userdetails,username)
            break
        else:
            print("Invalid Option")
    # method 2
    # print(f"Current Balance : {userdetails[-2]}")


#showProfile
def showprofile(userdetails,username):
    # print(userdetails)
    print("Profile Details 👇👇👇")
    print("----------------------------")
    print(f"Name : {userdetails[-1]} \nUsername : {userdetails[1]}\nAccount no : {userdetails[-3]}\nIFSC CODE : {userdetails[-5]}\nBank Name : {userdetails[4]}\nBranch Name : {userdetails[3]}")
    while True:
        option = int(input("Enter 1 for back to show features : "))
        if option==1:
            showfeatures(userdetails,username)
            break
        else:
            print("Invalid Option..")
        


#showfeatures 
def showfeatures(userdetails,username):
    print("1. Net Banking\n2. Show Profile\n3. Deposit\n4. Check Balance\n5. Exit")
    option = int(input("Enter Correct Option : "))
    match option:
        case 1:
            # print("NetBanking")
            netbanking(userdetails,username)
        case 2:
            # print("Show Profile")
            showprofile(userdetails,username)
        case 3:
            # print("Deposit")
            deposit(userdetails,username)
        case 4:
            # print("Check Balance")
            checkbalance(userdetails,username)
        case 5:
            return 0
        case _:
            print("Invalid Option ❌❌❌")
            showfeatures(userdetails,username)
#check user password
def checkuserpassword(username):
    print(f'Username : {username}')
    user_db_pass = list(conn.execute(f'''select password from AccountDetails  where username ="{username}"'''))[0][0]
    user_pass = input("Enter Password : ")
    if user_pass == user_db_pass:
        print("Login Successful ✅✅✅")
        userdetails = list(conn.execute(f'''select * from AccountDetails where username ="{username}"'''))
        userdetails = [i for i in userdetails[0]]
        showfeatures(userdetails,username)
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