'''
Net Banking

Features :->

1) Login 
2) Register
3) Add amount
4) Net Banking
5) Show Profile
6) Check Balance
'''
'''
Step 1 :
Register
Step 2 :
Login
1) username -- check whether username is correct or not -->false again user should ask username from user
2) password -- check whether the given password is correct or not.--again user should enter password
here after this will fetch user details based on username
showfeatures(userdetails)
Step 3 :
Show all the features :(userdetails)
option from user
1) Add amount (userdails)
2) Net Banking(userdetails)
3) Show Profile(userdetails)
4) Check Balance(userdetails)
other than any input user enters invalid options should print and again we should ask user option
Step 4 :
if user enters option 1
------------------------------------------
Add amount features will open(userdetails)
------------------------------------------
amount from user... 0<=amount<=10000:
fetch old balance from user 
add amount+old balance now this our current balance
we should update this current balance to that particular account
we should display old balance then after we should display current balance
option :
1) we to deposit again ? -- >amount --> oldbalance --> amount+oldbalace ==> store it into current balance
2) Go back to Show features
other options invalid options 
--------------------------------------------
Net Banking(userdetails)

Sender -----------> Receiver 
if user logged in via this mail id : abc@gmail.com
receiver maild : xyz@gmail.com
receiver mailid we should get from user
next check receiver maildid is present in the db or not 
otp--> 1232
u_otp --> 2343
again it will generate new otp for user then if user enter correct otp 
next ask amount from user if user enters 1000
sender(abc@):
Balance : 5000
Sent : 1000 to xyz@
Current : Balance - Sent
balance : 4000
receiver(xyz@):
Balance : 200
Current : Balance + amount(sent or receiver)
Balance : 1200
next we should call the checkbalance feature here
Options :
1) Again want to sent ?
2) Go back to show feature
-------------------------------------------
Show Profile(userdetails)
Account Name :
Account No : 
Address : 
Branch Name : 
Bank Name : 
IFSC Code :
Account Type :
Mobile No :
------------------------------------------
Check Balance(userdatils):
we should print balance here 
Options :
1) Back to Show Features
-------------------------------------------
'''