from socket import *
import struct

try:
    S = socket(AF_INET, SOCK_STREAM)
    host = '127.0.0.1'
    port = 8000
    S.connect((host, port))

    while True:
        # Send message length (4 bytes)
        Y = input("Client: ")
        msg_length = len(Y.encode('utf-8'))
        S.send(struct.pack('!I', msg_length))

        # Send message data
        S.send(Y.encode('utf-8'))

        # Receive response from the server
        # Receive message length (4 bytes)
        msg_length_bytes = S.recv(4)
        if not msg_length_bytes:
            print("Server closed the connection")
            break

        # Unpack message length
        msg_length = struct.unpack('!I', msg_length_bytes)[0]

        # Receive message data
        msg_data = S.recv(msg_length)

        print("Server:", msg_data.decode('utf-8'))

except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat is terminated")
finally:
    S.close()
