import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
print ("client host: %s" % host)
port = 9999

# connection to hostname on the port.
s.connect(('127.0.0.1', port))

# while loop to send data to the server
while True:
  data = input("Enter data to send to server: ")
  s.send(data.encode('ascii'))
  # receive data from the server
  msg = s.recv(1024)
  print("Message from server: %s" % msg.decode('ascii'))
  if data == 'exit':
    break
s.close()  
print('Connection closed')


