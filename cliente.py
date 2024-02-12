import socket
import threading
import sys

def receive_messages(client_socket):
    while True:
        try:
            # Recibir mensajes del servidor y mostrarlos
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Mensaje recibido: {message}")
        except socket.error as e:
            print(f"Error de conexión: {e}")
            break

# Configurar el cliente
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect(('127.0.0.1', 9999))
except socket.error as e:
    print(f"No se pudo conectar al servidor: {e}")
    sys.exit()

# Iniciar un hilo para recibir mensajes
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Enviar mensajes al servidor
while True:
    message = input("Ingrese un mensaje (o 'exit' para salir): ")
    client.send(message.encode('utf-8'))

    # Agregar una condición para salir del bucle
    if message.lower() == 'exit':
        break

# Cerrar el socket al salir
client.close()
