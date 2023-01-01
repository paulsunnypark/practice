import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999

# connection to hostname on the port.
s.connect(('127.0.0.1', port))

# receive data from the server
data = s.recv(1024)

# save the data to a file
with open('audio.wav', 'wb') as f:
    f.write(data)

# close the connection
s.close()
