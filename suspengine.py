import socket
import threading
import json

clientlist = []
userevents = {}

use = {}
prev = {}
limit = False
defaultlimit = 4096
debug = True
splitter = "[{//V//}]"

class User:
    userlist = []
    def __init__(self, client) -> None:
        self.client = client
        self.userdata = {}
    

    def save_variable(self, name, data):
        self.userdata[name] = data
    
    def call_variable(self, name):
        if name in self.userdata:
            return self.userdata[name]
        else:
            return None
    
    @classmethod
    def find_user(cls, client):
        for user in cls.userlist:
            if user.client == client:
                return user
        
        return None



def savevariable(name, data, client):

    user = User.find_user(client)
    if user is not None:
        user.save_variable(name, data)
        


def callvariable(name, client):
    user = User.find_user(client)
    if user is not None:
        return user.call_variable(name)


"""
def callvariablelist(name,data):
    global userdata
    global clientlist
    templist = []
    for c in clientlist:
        if name in userdata[str(c)]:
            if userdata[str(c)][name] == data:
                templist.append(c)
    return templist
"""

def addfunc(event,func):
    global use
    use[event] = func

def channel(args1):
    def otherchannel(function):
        global use
        use[args1] = function

    return otherchannel

def emit(event,message,client):
    global splitter
    tempdata = {}
    tempdata[event] = message
    tempdata['identify'] = event
    message = json.dumps(tempdata)+splitter

    print("Sending", message)
    try:
        client.send(message.encode('utf-8'))
    except:
        print("error")

def broadcast(event,message):
    global clientlist
    global splitter
    tempdata = {}
    tempdata[event] = message
    tempdata['identify'] = event
    message = json.dumps(tempdata)+splitter
    for c in clientlist:
        c.send(message.encode('utf-8'))

def disconnect(client):
    client.close()

def handleclient(c,addr):
    global clientlist
    global userevents
    global splitter
    global use
    global prev
    global limit
    global defaultlimit
    global debug
    while True:
        try:
            data = c.recv(defaultlimit)
            if not data:
                clientlist.remove(c)
                if 'disconnect' in use:
                    use['disconnect'](c,addr)
                break
        except:
            clientlist.remove(c)
            if 'disconnect' in use:
                use['disconnect'](c,addr)
            break
        stuff = []
        try:
            data = data.decode('utf-8')

            if not limit:
                data = prev[str(c)] + data
                stuff = data.split(splitter)
                if len(stuff) > 1:
                    prev[str(c)] = ""
                if not "" in stuff:
                    prev[str(c)] = stuff[len(stuff)-1]
                    del stuff[len(stuff)-1]
                    if debug:
                        print("Your packet is bigger than the default size limit")
                stuff.remove("")
            else:
                stuff = data.split(splitter)
                stuff.remove("")
        except:
            pass
        for s in stuff:
            #print(stuff)
            tempdat = json.loads(s)
            for keys in tempdat.keys():
                if keys in use:
                    threading.Thread(target=use[keys],args=[c,addr,tempdat[keys]]).start()
                    #print(userevents)


def server(host,port,**kwargs):
    s = socket.socket()
    s.bind((host,port))
    #Variables for kwargs
    slots = 20
    global limit
    global debug
    global defaultlimit
    #
    for stuff in kwargs.items():
        if stuff[0] == 'debug':
            debug = stuff[1]
            if debug:
                print('Debug Enabled')
        if stuff[0] == 'slots':
            slots = stuff[1]
            if debug:
                print('Your server can take ' + str(stuff[1]) + " connections.")
        if stuff[0] == 'limit':
            limit = stuff[1]
            if debug and limit == False:
                print('You have removed the limit on how big your packets can be')
        if stuff[0] == 'defaultlimit':
            defaultlimit = stuff[1]
            if debug:
                print('Your limit to how big a packet can be is ' + str(stuff[1]) + " bytes.")

    s.listen(slots)
    global clientlist
    global use
    global userdata
    global prev
    while True:
        c, addr = s.accept()
        clientlist.append(c)
        threading.Thread(target=handleclient,args=[c,addr]).start()
        user = User(c)
        User.userlist.append(user)
        prev[str(c)] = ""
        print(str(addr[0]) + " Connected To The Server From Port " + str(addr[1]))
        if 'connect' in use:
            use['connect'](c,addr)


#server("127.0.0.1",5001)
