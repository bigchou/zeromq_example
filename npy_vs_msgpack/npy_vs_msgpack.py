import msgpack
import numpy as np
import time

# prepare input
input = np.random.rand(1000,10000)
print("input.shape: ",input.shape)
data = input.tolist()

# Write msgpack file
start = time.time()
with open("data.msgpack", "wb") as outfile:
    packed = msgpack.packb(data)
    outfile.write(packed)
print("[WRITE MSGPACK]: ",time.time()-start,"sec(s)")

# Read msgpack file
start = time.time()
with open("data.msgpack", "rb") as data_file:
    byte_data = data_file.read()
print("[READ MSGPACK]: ",time.time()-start,"sec(s)")

data_loaded = msgpack.unpackb(byte_data)
print(data == data_loaded)

# Write numpy file
start = time.time()
np.save("data.npy",input)
print("[WRITE NPY]: ",time.time()-start,"sec(s)")

# Read numpy file
start = time.time()
input_loaded = np.load("data.npy")
print("[READ NPY]: ",time.time()-start,"sec(s)")

print(np.array_equal(input, input_loaded))

