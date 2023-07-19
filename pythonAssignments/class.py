
'''
class User:
    #Defined attributes of class
    name = "No Name Provided"
    email = " "
    password = "918273645"
    account = 0

    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")
#outside of the class you create an instance of the User class
new_user = User()
#Call the login method using the new object
new_user.login()
'''

'''
def __init__(self, name, email, password, account):
    self.name = name
    self.email = email
    self.password = password
    self.account = account
'''

'''
New_user = User("John Doe", "jdow@gmail.com", "p@ssw0rd", 1234)
'''

class GuildMember:  #creating class guild members
    name = "No Name Provided"   #creates attribute for class guild member
    rank = " "
    party = "freelancer"


class Adventurer(GuildMember):  #creates subclass of guild member
    alias = "NoName"    #creates attributes to Adventurer in addition to
    job = "freelancer"  #the ones inherited from the GuildMember class

class Merchant(GuildMember):
    trade = "goods"

class Knight(GuildMember):
    order = "NoOrder"
    expertise = "training"
    
    
    
    
