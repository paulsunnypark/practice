import socket
import cal 

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
print ("Server host: %s" % host)
port = 9999

# bind to the port
serversocket.bind(('127.0.0.1', port))

# queue up to 5 requests
serversocket.listen(5)
clientsocket,addr = serversocket.accept()

while True:
    # establish a connection
    # clientsocket,addr = serversocket.accept()
    # data from clientsocket    
    data = clientsocket.recv(1024)
    # print("Got a connection from %s" % str(addr))
    msg = f'The message from client is : {data.decode("ascii")}' 
    print (msg)
    clientsocket.send(msg.encode('ascii'))
    if data.decode('ascii') == 'calculate':
        calmsg = cal.calculate()
        msg = f'The message after calculation is : {calmsg}'
        clientsocket.send(msg.encode('ascii'))        
    elif data.decode('ascii') == 'exit':
        break

clientsocket.close()

# close the server socket
serversocket.close()









