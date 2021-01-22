import numpy as np
import msgpack_numpy as m
import zmq, cv2, msgpack, sys, time

start = time.time()
# prepare input
input = {"a":[100,200,300],"b":"hello","c":cv2.imread("input.jpg")}

# init zeromq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5575")
#print("object size:",sys.getsizeof(input))
msg = msgpack.packb(input, default=m.encode, use_bin_type=True)
print("object size:",sys.getsizeof(msg))
# send request
socket.send(msg, copy=False)
message = socket.recv()
print("RECEIVE RESPONSE FROM SERVER")
print(message.decode(encoding='UTF-8'))
socket.close()
print("time elapsed:", time.time()-start)
