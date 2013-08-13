#!/usr/bin/env python
import sys
sys.path.append('/home/long/project/mychatserver/src')
from userlist import User
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import json

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type = int)

userlist = User()

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user')
        passwd = self.get_argument('passwd')
        if (userlist.checkUser(str(user), str(passwd)) == True):
            friendlist = userlist.getFriendlist(user)
            content = json.dumps(friendlist)
        else:
            content = json.dumps(['passwd error'])
        self.write(content)

class SigninHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user')
        passwd = self.get_argument('passwd')
        userlist.addNewUser(str(user), passwd)
        content = json.dumps(['OK'])
        self.write(content)
        print 'New : ' + user

class GetMessageHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user')
        passwd = self.get_argument('passwd')
        friend = self.get_argument('friend')
        if (userlist.checkUser(str(user), str(passwd)) == True):
            message = userlist.getMessage(user, friend)
            if (message[0][0] != 0):
                message.insert(0,['OK'])
            else:
                message[0][0] = 'NO'
            print 'Get : ' + str(message)
            content = json.dumps(message)
            self.write(content)

class FriendlistHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user')
        passwd = self.get_argument('passwd')
        if (userlist.checkUser(str(user), str(passwd)) == True):
            friendlist = userlist.getFriendlist(user)
            content = json.dumps(friendlist)
            self.write(content)

class SendMessageHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user')
        passwd = self.get_argument('passwd')
        friend = self.get_argument('friend')
        message = self.get_argument('message')
        if (userlist.checkUser(str(user), str(passwd)) == True):
            userlist.addMessage(friend, user, message.encode("utf-8"))
            content = json.dumps([['OK']])
            self.write(content)

class AddFriendHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user')
        passwd = self.get_argument('passwd')
        friendsname = self.get_argument('friendsname')
        if (userlist.checkUser(str(user), str(passwd)) == True):
            userlist.addNewFriend(user, friendsname)
            content = json.dumps(['OK'])
            self.write(content)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r'/login', LoginHandler),
        (r'/signin', SigninHandler),
        (r'/friendlist', FriendlistHandler),
        (r'/addfriend', AddFriendHandler),
        (r'/get', GetMessageHandler),
        (r'/send', SendMessageHandler)
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
        
