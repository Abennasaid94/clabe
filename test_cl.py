import socket,os,requests
ip = requests.get('https://api.ipify.org').content.decode()
print('My Ip NAT: %s'%ip)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 0))
localip=s.getsockname()[0]
s.close()
print('My Local Ip: %s'%localip)
listen_client_sock=socket.socket()
ip,por='34.80.1.204',36234
try:
    listen_client_sock.connect((ip,por))
    connection_soc=listen_client_sock.makefile('wb')
    print('Connection success to: %s:%d'%(ip,por))
except Exception as e:
    pass
    print(e)
