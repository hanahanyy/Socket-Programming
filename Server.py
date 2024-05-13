from socket import *
import struct

try:
    S = socket(AF_INET, SOCK_STREAM)
    host = '127.0.0.1'
    port = 8000
    S.bind((host, port))
    S.listen(5)
    print("Server started listening for requests...")
    conn, addr = S.accept()
    print("Connection from:", addr[0])

    while True:
        # Receive message length (4 bytes)
        msg_length_bytes = conn.recv(4)
        if not msg_length_bytes:
            print("Client closed the connection")
            break

        # Unpack message length
        msg_length = struct.unpack('!I', msg_length_bytes)[0]

        # Receive message data
        msg_data = conn.recv(msg_length)

        print("Client:", msg_data.decode('utf-8'))

        Y = input("Server: ")

        # Send message length
        conn.send(struct.pack('!I', len(Y)))

        # Send message data
        conn.send(Y.encode('utf-8'))

except error as e:
    print(e)
except KeyboardInterrupt:
    print("Chat is terminated")
finally:
    S.close()
