import socket
import os
import threading

#UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target_ip = "127.0.0.1"
target_port = 9999
final_target = (target_ip, target_port)

# Creating a folder if it doesn't exist
folder_name = 'data_folder'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
print("Welcome to UDP chatroom!")


while True:
        msg = input("Please enter your message: ")
    
        new_msg = msg.encode('ascii')
    
        s.sendto(new_msg, final_target)
    
        # Creating a filename using the target IP address
        filename = os.path.join(folder_name, f"{target_ip}.txt")
    
        # Saving the message to a .txt file
        with open(filename, 'a') as file:
            file.write(msg + '\n')
            data = s.recvfrom(1024)
        received_msg = data[0].decode('ascii') 
        print("Received Message:", received_msg)




