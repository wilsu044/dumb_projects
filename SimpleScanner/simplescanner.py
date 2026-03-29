import socket

ip = "192.168.1.1"

print(f'loading {ip} \n')

for port in range(1, 1025):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	result = s.connect_ex((ip, port))

	if result == 0:
		print (f'open {port}')
	
	s.close()
	
