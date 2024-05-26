# python -m pip install timezonefinder pyaes pbkdf2 SpeechRecognition pydub
import socket,os,requests
ip = requests.get('https://api.ipify.org').content.decode()
print('My Ip NAT: %s'%ip)
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 0))
localip=s.getsockname()[0]
s.close()
print('My Local Ip: %s'%localip)
with socket.socket() as listen_client_sock:
    print('Wait for Connextion ...')
    while True:
            try:
                listen_client_sock.bind(('', 36234))
                listen_client_sock.listen()
                # print("Binding socket to port: "+str(server_port))
                break
            except Exception as e:
                time.sleep(1)
                print(e)
    while True:
        server_soc, server_address = listen_client_sock.accept()
        print('new ',server_address)
