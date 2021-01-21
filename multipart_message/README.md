

# Testing VIRTURAL ENV

conda activate [ENV]

Python 3.6 : zeromq

Python 2.7 : zeromq_py2

~~~~
# Python 3.6 v.s. Python 2.7
python server_py2.py # Python 2.7
python client.py # Python 3.6

# Python 3.6 v.s. Python 3.6
python server_py3.py # Python 3.6
python client.py # Python 3.6
~~~~


# Reference

1. [How to send both image(ndarray) and string data in single ZMQ send request](https://stackoverflow.com/questions/53049141/how-to-send-both-imagendarray-and-string-data-in-single-zmq-send-request)

2. [How to convert between bytes and strings in Python 3](https://stackoverflow.com/questions/14010551/how-to-convert-between-bytes-and-strings-in-python-3)

3. [Convert byte array back to numpy array](https://stackoverflow.com/questions/53376786/convert-byte-array-back-to-numpy-array)

4. [Converting int to bytes in Python 3](https://stackoverflow.com/questions/21017698/converting-int-to-bytes-in-python-3)

5. [Python3 How to make a bytes object from a list of integers](https://stackoverflow.com/questions/30658193/python3-how-to-make-a-bytes-object-from-a-list-of-integers)

6. [Changing bytes() (Python 3 string) output back to list of ints](https://stackoverflow.com/questions/20962350/changing-bytes-python-3-string-output-back-to-list-of-ints)

7. [python convert bytearray to numbers in list](https://stackoverflow.com/questions/28488080/python-convert-bytearray-to-numbers-in-list)

8. [How to display values larger than 255 in Bytes in Python 3](https://stackoverflow.com/questions/25499719/how-to-display-values-larger-than-255-in-bytes-in-python-3)

9. [How to convert bytes in a string to integers? Python](https://stackoverflow.com/questions/3255987/how-to-convert-bytes-in-a-string-to-integers-python)

10. [Convert dictionary to bytes and back again python?](https://stackoverflow.com/questions/19232011/convert-dictionary-to-bytes-and-back-again-python)

11. [使用 OpenCV 不存檔直接讀入 Flask 所傳進的圖片](https://cynthiachuang.github.io/Reading-Image-File-Without-Saving-It-Using-CV2-in-Flask/)

~~~~
import request
filestr = request.files['file'].read()
npimg = numpy.fromstring(filestr, numpy.uint8)
img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
~~~~

# Note

1. bytearray or bytes(...) should only store 0 through 255.

# TODO

1. [What is the most efficient way of sending a sequence of different data types with send_multipart() in ZMQ?](https://stackoverflow.com/questions/54047948/what-is-the-most-efficient-way-of-sending-a-sequence-of-different-data-types-wit)

