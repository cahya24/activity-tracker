class User:
    def __init__(self, userName, phoneNum):
        self.userName = userName
        self.phoneNum = phoneNum
        self.userId = 1

    def printUser(self):
        print(self.userName)
    

user1 = User("Adi", 123)
user2 = User("Ado", 456)