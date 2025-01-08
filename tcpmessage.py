# Server

import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)
print(f"服务器正在监听 {SERVER_HOST}:{SERVER_PORT}...")

clients = []


def handle_client(client_socket, client_address):
    print(f"新连接: {client_address}")
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"来自 {client_address} 的消息: {message}")
            
            broadcast_message(message, client_socket)
        except ConnectionResetError:
            break
    
    print(f"连接关闭: {client_address}")
    clients.remove(client_socket)
    client_socket.close()

# sned
def broadcast_message(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

# receive
def accept_connections():
    while True:
        client_socket, client_address = server_socket.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

# start
accept_connections()

#client

import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# 接收消息
def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            break

# send
def send_messages():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
