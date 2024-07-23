'''
InstagramProfile
step 1 :
create acoount with user_name,pwd,mail_id
step 2:
intialize follower and following count =0
step 3 : 
should write logic for follow
step 4 : 
should write logic for unfollow
step 5 :
display user details
'''
class InstagramProfile:
    def __init__(self,u_name,pwd,mailid):
        self.u_name=u_name
        self.pwd = pwd
        self.mailid = mailid
        self.following = 0
        self.followers = 0
    def follow(self,other_user):
        if self==other_user:
            print("Same users are not able to follow")
        else:
            self.following+=1
            other_user.followers+=1
    def unfollow(self,other_user):
        if self==other_user:
            print("Same users are not able to unfollow")
        else:
            if self.following>0 and other_user.followers>0:
                self.following-=1
                other_user.followers-=1
            else:
                print("Unable to unfollow...")
    def displayinfo(self):
        print(f"Username : {self.u_name}\nPassword : {self.pwd}\nMailId : {self.mailid}\nFollowers : {self.followers}\nFollowing : {self.following}")
user1 = InstagramProfile("User1","1234","user1@gmail.com")
user2 = InstagramProfile("User2","1234","user2@gmail.com")
# user1.displayinfo()
print("Follow ----> ")
user1.follow(user2)
user2.follow(user1)

user1.displayinfo()
print("--------------------------")
user2.displayinfo()

print("\nUnfollow -------->")
user1.unfollow(user2)
user1.displayinfo()
print("--------------------------")
user2.displayinfo()

'''
user1 --> user2
user1:
following count : 1
user2:
followers count : 1
user1---> user1
'''

        