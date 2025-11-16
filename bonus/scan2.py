# Python 2.x script

import socket

network = raw_input("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
ports = [21, 22, 23, 80, 443, 3306]
for host in range(1, 254):
    ip = "{}.{}".format(network, host)
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print "Host {} has port {} open".format(ip, port)
        sock.close()