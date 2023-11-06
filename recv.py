import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = "127.0.0.1"
server_port = 9999
s.connect((server_ip, server_port))

print("Welcome to the Multi-User Chatroom")

while True:
    msg = input("Please enter your message (To quit enter '/exit'): ")

    if msg == '/exit':
        print("Exiting the chatroom.")
        break

    new_msg = msg.encode('ascii')
    s.send(new_msg)

    response = s.recv(100)
    reply_msg = response.decode('ascii')
    print(f"Reply from the server: {reply_msg}")

s.close()
