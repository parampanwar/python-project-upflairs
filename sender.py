import socket
import os
import threading

# Function to handle each client
def handle_client(client_socket):
    while True:
        data = client_socket.recv(100)
        message = data.decode('ascii')
        if not data:
            break  # Connection closed by the client
        print(f"Message from {client_socket.getpeername()[0]}: {message}")

        directory_path = 'chat_users'
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        file_name = client_socket.getpeername()[0]

        with open(os.path.join('chat_users', file_name + '.txt'), 'a+') as f:
            f.write(f"{message}\n")

        response = input("Enter your reply: ")
        client_socket.send(response.encode('ascii'))

    client_socket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_ip = "192.168.1.58"
my_port = 9999
my_address = (my_ip, my_port)
s.bind(my_address)
s.listen(5)

print("Welcome to TCP Multi-User Chatroom")

while True:
    client_socket, client_address = s.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
