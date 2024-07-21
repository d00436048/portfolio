import socket

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_addr = '0.0.0.0'  # Listen on all available interfaces
server_port = 12345

# Bind the socket to the server address and port
server_socket.bind((server_addr, server_port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Server is listening on {server_addr}:{server_port}")

# Accept incoming connection
client_socket, client_addr = server_socket.accept()
print(f"Connection established with {client_addr}")

# Receive data from the client
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received message from {client_addr}: {data.decode()}")

    # Echo the message back to the client
    client_socket.sendall(data)

# Close the client socket
client_socket.close()

# Close the server socket
server_socket.close()
