import socket
# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# open the socket, i.e., listen on a certain port
server_addr = ''
server_port = 12000
s.bind((server_addr, server_port))
print("server is running...")
try:
    while True:
        # wait for request
        buffer = 2048
        msg, client_addr = s.recvfrom(buffer)

        msg = msg.decode('utf-8')
        # 1. parse msg, e.g., what is the filename requested?
        # 2. perform logic...
        # 3. build response
        # respond to request

        print(msg)
        s.sendto(bytes('PONG','utf-8'), client_addr)
except KeyboardInterrupt:
    print("\nServer stopped")
# close socket
s.close()
