# maak een chat programma tussen twee computers of via de localhost 
# sudo rechten om tcpdump te gebruiken
# maak een chat programma tussen twee computers of via de localhost


import socket
def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server gestart op {host}:{port}. Wacht op verbinding...")
    
    conn, addr = server_socket.accept()
    print(f"Verbonden met {addr}")
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Client: {data.decode()}")
        message = input("Server: ")
        conn.sendall(message.encode())
    
    conn.close()
    server_socket.close()
def start_client(host='localhost', port=12345):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Verbonden met server op {host}:{port}")
    
    while True:
        message = input("Client: ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Server: {data.decode()}")
    
    client_socket.close()
if __name__ == "__main__":
    choice = input("Start server (s) of client (c)? ").lower()
    if choice == 's':
        start_server()
    elif choice == 'c':
        start_client()
    else:
        print("Ongeldige keuze. Kies 's' voor server of 'c' voor client.")
# This code implements a simple chat program using sockets in Python.
# The server listens for incoming connections and the client connects to the server.
# The server and client can send and receive messages until one of them decides to exit.
# The server can be started on one machine and the client can connect to it from another machine or the same machine using localhost.
# The server and client communicate over a specified host and port.
# The server waits for a client to connect, and once connected, it can receive messages from the client and send responses back.
# The client can send messages to the server and receive responses until it sends 'exit' to terminate the connection.
# The program uses the socket library to handle network communication.
# The server and client can be run on the same machine or different machines on the same network.
# The server listens for incoming connections and the client connects to the server.
# The chat program allows for real-time communication between two parties.
# The server can handle multiple messages in a single session until one party decides to exit.
# The program is a basic implementation of a chat application using Python's socket library.
# The chat program can be extended with features like message history, user authentication, or GUI interfaces.
# The current implementation is a console-based chat application.
# It demonstrates the basic principles of socket programming in Python.
# The server and client can be run in separate terminal windows or on different machines.
# The program can be used for learning purposes or as a foundation for more complex chat applications.
# The chat program can be modified to include error handling, logging, or encryption for secure communication.
# The current implementation is a simple text-based chat application.
# It can be used as a starting point for building more advanced chat applications.
# The chat program can be run in a local network or over the internet with proper port forwarding.
# The server can handle multiple clients by using threading or asynchronous programming.
# The client can be run multiple times to simulate multiple users chatting with the server.
# The chat program can be enhanced with features like private messaging, group chats, or file sharing.
# The current implementation is a basic chat application that can be improved with additional features.
# The chat program can be used for educational purposes to understand socket programming in Python.
# The server and client can be run on different machines to test network communication.
# The chat program can be extended with features like user registration, login, and message encryption.
# The current implementation is a simple chat application that can be used for learning and experimentation.
# The chat program can be run in a local environment or deployed on a server for remote access.
# The server can be modified to handle multiple clients simultaneously using threading or async I/O.
# The client can be enhanced with a graphical user interface (GUI) for better user experience.
# The chat program can be used as a foundation for building more complex applications like online games or collaborative tools.