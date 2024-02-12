import socket
import threading
import queue

# Crear una cola para mensajes
message_queue = queue.Queue()

# Función para manejar la conexión de un cliente
def handle_client(client_socket):
    while True:
        # Recibir mensaje del cliente
        message = client_socket.recv(1024).decode('utf-8')

        if not message:
            # Si el mensaje está vacío, el cliente se desconectó
            print(f"Cliente {client_socket.getpeername()} se desconectó.")
            clients.remove(client_socket)
            break

        # Imprimir información del mensaje recibido
        print(f"Mensaje recibido de {client_socket.getpeername()}: {message}")

        # Agregar el mensaje a la cola
        message_queue.put(message)

        # Enviar mensajes en la cola a todos los clientes conectados
        while not message_queue.empty():
            queued_message = message_queue.get()
            for client in clients:
                if client != client_socket:  # No enviar el mensaje de vuelta al remitente
                    client.send(queued_message.encode('utf-8'))
                    print(f"Mensaje enviado a {client.getpeername()}: {queued_message}")

# Configurar el servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(5)

print("El servidor está escuchando en el puerto 9999...")

# Lista para almacenar clientes conectados
clients = []

while True:
    client_socket, addr = server.accept()
    clients.append(client_socket)

    # Imprimir información del cliente recién conectado
    print(f"Nuevo cliente conectado desde {addr}.")

    # Iniciar un hilo para manejar la conexión del cliente
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
