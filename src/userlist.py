#!/usr/bin/env python

class User(object):
    def __init__(self):
        self.userlist = {'long':'123456','wanzi':'123456'}
        self.friendlist = {'long':['wanzi'],
            'wanzi':['long'],
        }
        self.message = {
           #'from':{'to':[['message','owner']]}
            'long':{'wanzi':[['hello','wanzi']]},
            'wanzi':{'long':[['nihao','long']]}
        }
        
    def addNewUser(self, username, passwd):
        self.userlist[username] = passwd
        self.friendlist[username] = ['long']
        self.message[username] = {'long':[]}
        self.message[username]['long'].append(['welcome to use MyChat.','long'])
        
    def checkUser(self, username, passwd):
        if username in self.userlist:
            if (self.userlist[username] == passwd):
                return True
        return False

    def addNewFriend(self, username, friendsname):
        self.friendlist[username].append(friendsname)

    def getFriendlist(self, username):
        return self.friendlist[username]

    def addMessage(self, To, From, message):
        if (From not in self.message):
            self.message[From] = {}
        if (To not in self.message[From]):
            self.message[From][To] = []
        self.message[From][To].append([message,From])
        if (To not in self.message):
            self.message[To] = {}
        if (From not in self.message[To]):
            self.message[To][From] = []
        self.message[To][From].append([message,From])

    def getMessageAll(self, username):
        message = self.message[username]
        self.message.pop(username)
        return message

    def getMessage(self, username, friendsname):
        if friendsname not in self.message[username]:
            return [[0]]
        message = self.message[username][friendsname]
        self.message[username].pop(friendsname)
        return message
