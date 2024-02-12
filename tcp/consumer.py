import socket
import threading

HOST = '0.0.0.0'  # Ouvir em todas as interfaces
PORT = 65430
BUFFER_SIZE = 10

# Create a semaphore
semaphore = threading.Semaphore()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('Aguardando conexões...')
        while True:
            conn, addr = s.accept()
            print('Caminhão conectado por', addr)
            with conn:
                while True:
                    data = conn.recv(BUFFER_SIZE)
                    if not data:
                        print('Caminhão desconectado por', addr)
                        break
                    peso = float(data.decode())
                    print('Peso recebido:', peso)
                      # Acquire the semaphore to lock the file
                    semaphore.acquire()
                    # lock file
                    try:
                        # get actual weight in pesos.txt
                        peso_atual = 0
                        with open('pesos.txt', 'r') as file:
                            peso_atual = float(file.read())
                        
                        # check if weight is valid
                        # sum
                        peso_atual += peso
                        
                        # save
                        with open('pesos.txt', 'w') as file:
                            file.write(str(peso_atual))
                    except Exception as e:
                        print('Erro ao salvar peso:', e)
                        break
                    finally:
                        # Release the semaphore to unlock the file
                        semaphore.release()
                 
                    conn.sendall(b'Peso recebido com sucesso')

if __name__ == "__main__":
    main()
