import socket
import _pickle as pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "0.0.0.0.0"
        self.port = 1512
        self.addr = (self.host, self.port)

    def connect(self, name, host):
        self.host = host
        self.addr = (self.host, self.port)
        self.client.connect(self.addr)
        self.client.send(str.encode(name))

        try:


            reply = self.client.recv(2048 * 4)
            try:
                reply = pickle.loads(reply)
                print("received initial data: ", reply)
            except Exception as e:
                print(e)

            return reply
        except socket.error as e:
            print(e)


    def disconnect(self):
        self.client.close()

    def send(self, data, pick=False):

        try:
            if pick:
                self.client.send(pickle.dumps(data))
            else:
                self.client.send(str.encode(data))
            reply = self.client.recv(2048*4)
            try:
                reply = pickle.loads(reply)
                #print("received data: ",reply)

            except Exception as e:
                print(e)

            return reply
        except socket.error as e:
            print(e)