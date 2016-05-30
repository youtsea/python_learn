import os

fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)
f = open(fd, 'wt', closefd=False)
f.write('hello world\n')
f.close()

from socket import socket, AF_INET, SOCK_STREAM


def echo_client(client_sock, addr):
    print 'Got Connection from', addr

    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)

    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)