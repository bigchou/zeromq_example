import zmq, pdb, cv2, json
import numpy as np 
print("START SERVER")
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5585")
while True:
    output = socket.recv_multipart()
    data1, data2, shape, data3, size, data4 = output
    data1 = data1.decode(encoding='UTF-8')
    shape = list(shape)
    data2 = np.frombuffer(data2, dtype=np.float64)#dtype should be shown explicitly
    data2 = data2.reshape(shape)
    size = np.frombuffer(size, dtype=np.int64)#dtype should be shown explicitly
    data3 = np.frombuffer(data3, dtype=np.uint8)#dtype should be shown explicitly
    data3 = data3.reshape(size)
    print("[output data1]")
    print(data1)
    print("[output data2]")
    print(data2)
    print(data2.dtype)
    print("[output data3]")
    print(data3.shape)
    ans = cv2.imread("input.jpg")
    print("IS INPUT THE SAME? ",np.array_equal(ans,data3))
    print("[output data4]")
    data4 = json.loads(data4.decode('utf-8'))
    print(data4["a"])
    print(data4["b"])
    print(np.array_equal(ans,np.array(data4["c"])))
    socket.send(str("MY_RESPONSE").encode('UTF-8'))#require btye object instead of str
