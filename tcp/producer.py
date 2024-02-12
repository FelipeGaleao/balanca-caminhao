import socket
import random
import time

HOST = 'consumer'  # Endereço do terminal de pesagem na rede Docker
PORT = 65430
BUFFER_SIZE = 3024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print('Tentando se conectar ao terminal de pesagem...')
        while True:
            try:
                s.connect((HOST, PORT))
                break
            except ConnectionRefusedError:
                pass

        print('Conexão estabelecida com o terminal de pesagem.')
        
        print("Digite o peso permitido: ")
        # get random weight
        peso = random.randint(20000, 40000)
        print('Peso gerado:', peso)
        peso = str(peso)
        try:
            s.sendall(peso.encode())
            data = s.recv(BUFFER_SIZE)
            print('Resposta do terminal de pesagem:', data.decode())
        except ConnectionResetError:
            print('Conexão encerrada pelo terminal de pesagem')

if __name__ == "__main__":
    main()
    while True:
        main()