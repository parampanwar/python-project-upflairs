import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_ip = "127.0.0.1"
my_port = 9999
my_address = (my_ip, my_port)
s.bind(my_address)
print("Welcome to UDP chatroom!")
clients = {}
connected = False  # To keep track of whether a client is connected

def receive_messages():
    global connected  # Use the global variable
    while True:
        data, client_address = s.recvfrom(100)
        new_data = data
        received_msg = new_data.decode('ascii')
        print("Received Message:", received_msg)

        if not connected:
            print(f"Client {client_address} connected.")
            connected = True

        # Get a reply message from the user
        reply_msg = input("Reply: ")

        # Encode and send the reply message back to the sender
        s.sendto(reply_msg.encode('ascii'), client_address)

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()
