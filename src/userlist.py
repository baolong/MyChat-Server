#!/usr/bin/env python
#_*_ coding: utf-8

class User(object):
    def __init__(self):
        self.userlist = {
           #'username' : 'passwd'
            'long':'123456',
            'wanzi':'123456'
        }
        self.friendlist = {
           #'username' : ['friendsname']
            'long':['wanzi'],
            'wanzi':['long'],
        }
        self.message = {
           #'from':{'to':[['message','owner']]}
            'long':{'wanzi':[['hello','wanzi']]},
            'wanzi':{'long':[['nihao','long']]}
        }
        
    def addNewUser(self, username, passwd):
        if username not in self.userlist:
            self.userlist[username] = passwd
            self.friendlist[username] = ['long']
            self.message[username] = {'long':[]}
            self.message[username]['long'].append(['欢迎使用MyChat聊天工具.','long'])
            return 0
        else:
            return -1
        
    def checkUser(self, username, passwd):
        if username in self.userlist:
            if (self.userlist[username] == passwd):
                return True
        return False

    def addNewFriend(self, username, friendsname):
        if username == friendsname:
            return 1
        if (friendsname in self.userlist):
            self.friendlist[username].append(friendsname)
            self.friendlist[friendsname].append(username)
            return 0
        else:
            return 2

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
