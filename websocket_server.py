#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import socket
import os
'''
This is a simple Websocket Echo server that uses the Tornado websocket handler.
Please run `pip install tornado` with python of version 2.7.9 or greater to install tornado.
This program will echo back the reverse of whatever it recieves.
Messages are output to the terminal for debuggin purposes. 
''' 
 
class WSHandler(tornado.websocket.WebSocketHandler):

    connections = set()

    def open(self):
        print ('new connection')
        self.connections.add(self)
      
    def on_message(self, message):
        print ('message received:  %s' % message)
        # Reverse Message and send it back
        print ('sending back message to: ')
        print (self.connections)
        print ('sending back message: %s' % message)

        for con in self.connections:
            try:
                con.write_message(message) 
                print ("message for client sent")
            except:
                print ("client disconnected")
 
    def on_close(self):
        print ('connection closed')
 
    def check_origin(self, origin):
        return True


 
application = tornado.web.Application([
    (r"/websocket", WSHandler),
])
 
if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(os.environ.get("PORT", 5000))
    myIP = socket.gethostbyname(socket.gethostname())
    print ('*** Websocket Server Started at %s***' % myIP)
    tornado.ioloop.IOLoop.instance().start()








