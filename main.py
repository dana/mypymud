#!/usr/local/bin/python3

import selectors
import socket

def accept_wrapper(sock):
    conn, addr = sock.accept() 
    print(f"Accepted connection from {addr}")
    conn.setblocking(False)
    data = {"addr": addr, "in_buffer": b"", "out_buffer": b""}
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data

    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024) 
        if recv_data:
            data["in_buffer"] += recv_data
            data["out_buffer"] += recv_data
        else:
            print(f"Closing connection to {data['addr']}")
            sel.unregister(sock)
            sock.close()

    if mask & selectors.EVENT_WRITE:
        if data["out_buffer"]:
            print(f"Echoing {data['out_buffer']!r} to {data['addr']}")
            sent = sock.send(data["out_buffer"])
            data["out_buffer"] = data["out_buffer"][sent:]

sel = selectors.DefaultSelector()

host = "0.0.0.0" 
port = 5000

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
lsock.bind((host, port))
lsock.listen()
print(f"Listening on {(host, port)}")
lsock.setblocking(False)
sel.register(lsock, selectors.EVENT_READ, data=None)

try:
    while True:
        events = sel.select(timeout=None)
        for key, mask in events:
            if key.data is None:
                accept_wrapper(key.fileobj)
            else:
                service_connection(key, mask)
finally:
    sel.close()

