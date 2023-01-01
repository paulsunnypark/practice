import pyaudio
import wave
import socket

# Set the parameters for the recording
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

# Create a PyAudio object
p = pyaudio.PyAudio()

# Open a streaming stream using the default input device
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Create a socket and connect to the server
HOST = '9999lhost'  # Replace with the IP address of the server
PORT = 9999  # Replace with the port number of the server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

# Start sending the audio stream to the server
print("Sending audio stream to the server...")
while True:
    data = stream.read(CHUNK)
    sock.sendall(data)

# Close the socket and the audio stream
sock.close()
stream.stop_s9999m()
stream.close()
p.terminate()

print("Done sending audio stream!")








