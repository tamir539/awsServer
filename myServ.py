import socket
import random
from datetime import datetime


# create the server
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', 8451))
server_socket.listen(2)

while True:
    # try to connect to the server
    (client_socket, client_addres) = server_socket.accept()
    print(f'{client_addres[0]} - connected')
    while True:
        try:
            # try to recive massage from the client
            data = client_socket.recv(4).decode()
            print(data)
        except Exception as e:
            break
        else:
            if data != '':
                # check what is the comand and answer in accordance
                if data.lower() == 'name':
                    # respone the name of the server
                    respone = 'serv'
                elif data.lower() == 'rand':
                    # respone random number between 1 to 11
                    respone=str(random.randint(1, 11))
                elif data.lower() == 'exit':
                    # disconnect the client
                    break
                elif data.lower() == 'time':
                    # find the curennt date and time
                    now = datetime.now()
                    respone = now.strftime("%d/%m/%Y %H:%M:%S")
                try:
                    #try to send answer to the client
                    bytes_to_send = len(respone)
                    bytes_to_send = str(bytes_to_send).zfill(2)
                    client_socket.send(str(bytes_to_send).encode())
                    client_socket.send(respone.encode())
                except Exception:
                    break
            else:
                break
    print(f'{client_addres[0]} - disconected')
    client_socket.close()
    server_socket.close()
