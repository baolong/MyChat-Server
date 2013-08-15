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
        user = self.get_argument('user').encode('utf-8')
        passwd = self.get_argument('passwd').encode('utf-8')
        if (userlist.checkUser(user, passwd) == True):
            friendlist = userlist.getFriendlist(user)
            content = json.dumps(friendlist)
            self.write(content)
        else:
            raise tornado.web.HTTPError(400, reason='username or passwd error')

class SigninHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user').encode('utf-8')
        passwd = self.get_argument('passwd').encode('utf-8')
        if (0 == userlist.addNewUser(user, passwd)):
            raise tornado.web.HTTPError(200, reason='signin success')
        else:
            raise tornado.web.HTTPError(400, reason='username is exist.')

class GetMessageHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user').encode('utf-8')
        passwd = self.get_argument('passwd').encode('utf-8')
        friend = self.get_argument('friend').encode('utf-8')
        if (userlist.checkUser(user, passwd) == True):
            message = userlist.getMessage(user, friend)
            if (message[0][0] != 0):
                content = json.dumps(message)
                self.write(content)
            else:
                raise tornado.web.HTTPError(400, reason='no message')

class FriendlistHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user').encode('utf-8')
        passwd = self.get_argument('passwd').encode('utf-8')
        if (userlist.checkUser(user, passwd) == True):
            friendlist = userlist.getFriendlist(user)
            content = json.dumps(friendlist)
            self.write(content)

class SendMessageHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user').encode('utf-8')
        passwd = self.get_argument('passwd').encode('utf-8')
        friend = self.get_argument('friend').encode('utf-8')
        message = self.get_argument('message').encode('utf-8')
        if (userlist.checkUser(user, passwd) == True):
            userlist.addMessage(friend, user, message)
            raise tornado.web.HTTPError(200, 'send message success')

class AddFriendHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user').encode('utf-8')
        passwd = self.get_argument('passwd').encode('utf-8')
        friendsname = self.get_argument('friendsname').encode('utf-8')
        if (userlist.checkUser(user, passwd) == True):
            err = userlist.addNewFriend(user, friendsname)
            if (2 ==err):
                raise tornado.web.HTTPError(400, reason='user is not exist')
            if (1 == err):
                raise tornado.web.HTTPError(400, reason='can not add yourself.')

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
        
