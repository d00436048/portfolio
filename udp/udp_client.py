import time
import socket
# create socket

udp_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_addr = ''
server_port = 12000

#ping server
try:
    while True:
        st = time.time()

        udp_s.sendto(bytes('PING', 'utf-8'), (server_addr, server_port))


        data, addr = udp_s.recvfrom(1024)

        data = data.decode("utf-8")

        et = time.time()
        rtt = (et - st) * 1000

        print(f'{data} RTT: {rtt:.2f} ms')

        time.sleep(1)
except KeyboardInterrupt:
    print("\nClient stopped")

# close socket
udp_s.close()
