import zmq
import numpy as np
import msgpack
import msgpack_numpy as m
import cv2

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5575")
while True:
    task = socket.recv()
    task = msgpack.unpackb(task, object_hook= m.decode, use_list=False,  max_bin_len=50000000, raw=False)
    print(task["a"])
    print(task["b"])
    print(task["c"].shape)
    ans = cv2.imread("input.jpg")
    print(np.array_equal(ans,task["c"]))
    socket.send(str("MY_RESPONSE").encode('UTF-8'))
