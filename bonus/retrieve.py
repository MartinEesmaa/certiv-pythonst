import socket

ip = raw_input("Enter the IP address of the host: ")
port = 80 # HTTP port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.connect((ip, port))
s.sendall("GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(ip))
response = s.recv(4096)
print response
s.close()
