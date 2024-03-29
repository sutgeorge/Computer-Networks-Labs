import socket, struct

"""
    1. The client takes a string from the command line and sends it to the server.
       The server interprets the string as a command with its parameters. It executes
       the command and returns the standard output and the exit code to the client.
"""

while True:
    try:
        socket_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print("Error creating socket: {}".format(e))

    socket_fd.connect(("192.168.1.9", 9999))

    command = input("$ ")
    if command == "exit":
        socket_fd.close()
        break
    socket_fd.send(command.encode())

    response_size = socket_fd.recv(4)
    response_size = struct.unpack('!I', response_size)[0]
    result = socket_fd.recv(response_size).decode()
    print("{}\n".format(result))
