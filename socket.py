import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.2.67.114", 35000))

try:
    msj='holo'.encode()
    print('Mensaje enviado',msj)
    s.send(msj)

    amount_recived=0
    amount_expected=len(msj)
    
    while amount_recived<amount_expected:
        data=s.recv(16)
        amount_recived+=len(data)
        print ('Reciviendo', data)
        
finally:
    print('Cerrando')
    s.close()
