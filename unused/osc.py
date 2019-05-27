from OSC import OSCClient, OSCMessage, OSCServer
import time, threading


#server = OSCServer( ('localhost', 7110))

#def callback(path, tags, args, source):
#    print('works')
#    print(path)
#    print(tags)
#    print(args)
#    print(source)

#st = threading.Thread(target = server.serve_forever)
#st.start()
#server.serve_forever
#server.addMsgHandler( "/rstateong", callback)



client = OSCClient()
client.connect( ("localhost", 9951) )


m = OSCMessage("/ping")
m.append('localhost')
m.append(7110)
m.append('/pong')
client.send(m)


print('done')
