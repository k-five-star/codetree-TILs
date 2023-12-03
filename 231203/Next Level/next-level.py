class user:
    def __init__(self, _id = "codetree", level = "10"):
        self._id = _id
        self.level = level

    def userPrint(self):
        print("user " + self._id + " lv " + self.level)

userId, userLv = tuple(input().split())

user1 = user()
user2 = user(userId, userLv)

user1.userPrint()
user2.userPrint()