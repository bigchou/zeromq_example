import json, zmq, sys
import numpy as np
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5585")
while True:
    output = socket.recv()
    #print(sys.getsizeof(output))
    output = output.decode('utf-8')
    #print(sys.getsizeof(output))
    output = json.loads(output)
    #print(sys.getsizeof(output))
    #print(np.array(output["c"]).shape)
    socket.send(str("MY_RESPONSE").encode('UTF-8'))#require btye object instead of str
