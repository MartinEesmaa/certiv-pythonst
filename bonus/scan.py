# Original code:

"""
# Script to ping all IP addresses in a /24 subnet
import os

network = input ("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
print(network)

# Iterate over all usable IPs in this subnet
for host in range (1, 254):
    print("Pinging " + network + "." + str(host))
    os.system("ping -c 2 " + network + "." + str(host))
"""

# Please note to run Python 2.x, use the following code:

import os
network = raw_input("Enter first 3 numbers of IP network, e.g. 1.2.3: ")
print network
for host in range(1, 254):
    ip = "{}.{}".format(network, host)
    response = os.system("ping -c 2 {} > /dev/null 2>&1".format(ip))
    if response == 0:
        print "Host {} is active".format(ip)
