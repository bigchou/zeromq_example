import sys, json, zmq, cv2, time
import numpy as np

start = time.time()
# prepare input
input = {"a":[100,200,300],"b":"hello","c":cv2.imread("input.jpg").tolist()}

# init zeromq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5585")
#print("object size:",sys.getsizeof(input))
#msg = json.dumps(input)
#print("object size:",sys.getsizeof(msg))
#msg = msg.encode('utf-8')
#print("object size:",sys.getsizeof(msg))
msg = json.dumps(input).encode('utf-8')
print("object size:",sys.getsizeof(msg))
message = socket.send(msg)
message = socket.recv()
print("RECEIVE RESPONSE FROM SERVER")
print(message.decode(encoding='UTF-8'))
socket.close()
print("time elapsed:", time.time()-start)

