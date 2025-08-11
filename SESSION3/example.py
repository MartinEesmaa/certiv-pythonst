HTTP=80;
SMTP=25;
FTP=21;
port = int(input("Enter the port number:"))
if port < 80 and port <= 1024:
	print("Targets to common number")

if (port==HTTP):
	print("Target to HTTP attack")