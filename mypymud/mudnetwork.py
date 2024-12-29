import selectors
import socket
import time

class MUDNetwork:
    def __init__(self):
        self.all_connections = []
        self.last_tick = time.time()

    def _send_all_data(self):
        for c in self.all_connections:
            if c["data"]["out_buffer"]:
                if c["conn"].fileno() > 0:
                    sent = c["conn"].send(c["data"]["out_buffer"])
                    c["data"]["out_buffer"] = c["data"]["out_buffer"][sent:]

    def _process_all_data(self):
        for read_conn in self.all_connections:
            if read_conn["data"]["in_buffer"]:
                for s in self.all_connections:
                    s["data"]["out_buffer"] += read_conn["data"]["in_buffer"]
                read_conn["data"]["in_buffer"] = b''


    def do_tick(self):
        now_tick = time.time()
        next_tick = self.last_tick + 0.1
        if now_tick < next_tick:
            return(None)
        self.last_tick = now_tick
        print("do_tick")
        self._send_all_data()
        self._process_all_data()

    def _accept_wrapper(self, sock):
        conn, addr = sock.accept()
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        data = {"addr": addr, "in_buffer": b"", "out_buffer": b""}
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)
        self.all_connections.append({"conn":conn, "events":events, "data":data})

    def _service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data

        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)
            if recv_data:
                data["in_buffer"] += recv_data
            else:
                print(f"Closing connection to {data['addr']}")
                self.sel.unregister(sock)
                sock.close()

        #if mask & selectors.EVENT_WRITE:
        #    if data["out_buffer"]:
        #        print(f"Echoing {data['out_buffer']!r} to {data['addr']}")
        #        sent = sock.send(data["out_buffer"])
        #        data["out_buffer"] = data["out_buffer"][sent:]


    def bind(self):
        self.sel = selectors.DefaultSelector()

        host = "0.0.0.0"
        port = 5000

        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.lsock.bind((host, port))
        self.lsock.listen()
        print(f"Listening on {(host, port)}")
        self.lsock.setblocking(False)
        self.sel.register(self.lsock, selectors.EVENT_READ, data=None)


    def loop(self):
        try:
            while True:
                events = self.sel.select(timeout=0.1)
                for key, mask in events:
                    if key.data is None:
                        self._accept_wrapper(key.fileobj)
                    else:
                        self._service_connection(key, mask)
                self.do_tick()
        finally:
            self.sel.close()

