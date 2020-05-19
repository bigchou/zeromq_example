"""
The script is modified based on the ZEROMQ example script
To learn more, please see https://zeromq.org/languages/python/
"""
import zmq, os


context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

src = "imgs"
for request in os.listdir(src):
    request = os.path.join(src,request)
    print("Sending request %s …" % request)
    socket.send(str(request).encode())#require btye object instead of str

    #  Get the reply.
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
