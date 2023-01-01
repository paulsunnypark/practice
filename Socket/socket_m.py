import socket
import cal

def start_server(host, port):
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind to the port
    serversocket.bind((host, port))

    # queue up to 5 requests
    serversocket.listen(5)

    print(f"Listening for connections on {host}:{port}...")
    # accept incoming connections
    clientsocket, addr = serversocket.accept()
    print(f"Got a connection from {addr}")

    while True:
        # receive data from the client
        data = clientsocket.recv(1024)
        data = data.decode("ascii")

        # handle the client's request
        if data == "calulate":
            # perform the calculation and send the result to the client
            result = cal.calculate()
            clientsocket.send(f"The result is: {result}".encode("ascii"))
        elif data == "exit":
            # disconnect the client
            clientsocket.send(b"Disconnecting...")
            break
        else:
            # send an error message to the client
            # clientsocket.send(b"Invalid request")
            msg = f'The message from client is : {data}' 
            print (msg)
            clientsocket.send(msg.encode('ascii'))
        
        clientsocket.close()

    # close the server socket
    serversocket.close()

if __name__ == "__main__":
    # get the host and port from the user
    host = input("Enter host (leave blank for 'localhost'): ") or "localhost"
    port = int(input("Enter port: ") or 9999)

    start_server(host, port)
