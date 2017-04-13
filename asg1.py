#!/usr/bin/python
import sys

import Queue
import threading
import urllib2

import socket
import time

def get_url(q, url):
    urllib2.urlopen(url).read()
    q.put(url)

def start_TCP_server(q, ip, port):
    sock = socket.socket(socket.AF_INET,
        socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip, port))
    sock.listen(1)
    while True:
        stream, addr = sock.accept();
        data = stream.recv(1024);
        q.put(int(data))
        stream.close();

def send_TCP_message(addr, message):
    connected = False
    while not connected:
        try:
            sock = socket.socket(socket.AF_INET,
                socket.SOCK_STREAM)
            sock.connect(addr)
            sock.sendall(str(message))
            connected = True
        except socket.error:
            pass;
        finally:
            sock.close()

def go(port, filename):
    TCP_IP = "127.0.0.1"
    TCP_PORT = int(port);

    q = Queue.Queue();

    t = threading.Thread(target=start_TCP_server, args=(q,TCP_IP, TCP_PORT))
    t.daemon = True
    t.start()

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    count = 0;
    for i in content:
        words = i.split();
        if words[0] == "receive":
            g = q.get()
            if count > g:
                count = count + 1;
            else:
                count = g + 1;
        elif words[0] == "call":
            addr = (words[1], int(words[2]))
            count = count + 1
            send_TCP_message(addr, count)
        else:
            count = count + 1;
        sys.stdout.write(str(count) + ' ');

if __name__ == "__main__":
    port = sys.argv[1];
    filename = sys.argv[2];
    go(port, filename)
