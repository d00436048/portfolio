import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_addr = '0.0.0.0'  # Replace 'server_public_ip' with the public IP address of the server
server_port = 12345

# Connect to the server
client_socket.connect((server_addr, server_port))
print(f"Connected to server at {server_addr}:{server_port}")

# Send data to the server
message = "Hello, server!"
client_socket.sendall(message.encode())

# Receive response from the server
response = client_socket.recv(1024)
print(f"Received response from server: {response.decode()}")

# Close the socket
client_socket.close()
