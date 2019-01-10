from OSC import OSCClient, OSCMessage, OSCServer
import time, threading


server = OSCServer( ('localhost', 7110))

def callback(path, tags, args, source):
    print('works')
    print(path)
    print(tags)
    print(args)
    print(source)

server.addMsgHandler( "/pong", callback)
st = threading.Thread(target = server.serve_forever)
st.start()



