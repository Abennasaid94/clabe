import socket,os,requests
listen_client_sock=socket.socket()
ip,por='34.80.1.204',36234
try:
    listen_client_sock.connect((ip,por))
    connection_soc=listen_client_sock.makefile('wb')
    print('Connection success to: %s:%d'%(ip,por))
except Exception as e:
    pass
    print(e)
