import zmq, sys, msgpack
import msgpack_numpy as m

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5575")
while True:
    task = socket.recv()
    #print("object size: ",sys.getsizeof(task))
    task = msgpack.unpackb(task, object_hook= m.decode, use_list=False,  max_bin_len=50000000, raw=False)
    socket.send(str("MY_RESPONSE").encode('UTF-8'))
