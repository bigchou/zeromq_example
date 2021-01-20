import zmq, cv2
import numpy as np

# prepare input
data1 = str("Hello World")
data2 = np.array([[0.3,0.4],[0.5,0.6]])
print("[input data1]")
print(data1)
print("[input data2]")
print(data2)
print(data2.dtype)
shape = list(data2.shape)
data2 = data2.reshape(shape)
print("[input data3]")
data3 = cv2.imread("input.jpg")
print(data3.shape,data3.dtype)
size = np.array(list(data3.shape),dtype=np.int64)
data3 = data3.reshape(size)


# init zeromq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5585")
print("SEND REQUEST")
socket.send_multipart([
    data1.encode(encoding='UTF-8'),
    data2.tobytes(),
    bytes(shape),
    data3.tobytes(),
    size.tobytes()
])
message = socket.recv()
print("RECEIVE RESPONSE FROM SERVER")
print(message.decode(encoding='UTF-8'))
socket.close()
