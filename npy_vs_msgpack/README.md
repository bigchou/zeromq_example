~~~~
>>> python npy_vs_msgpack.py 
# Python 2.7 Result
('input.shape: ', (1000, 10000))
('[WRITE MSGPACK]: ', 23.16072988510132, 'sec(s)')
('[READ MSGPACK]: ', 0.03656315803527832, 'sec(s)')
True
('[WRITE NPY]: ', 0.14667391777038574, 'sec(s)')
('[READ NPY]: ', 0.013184070587158203, 'sec(s)')
True
>>> ls -lh
-rw-r--r--  1 timmy  staff    86M Jan 21 17:54 data.msgpack
-rw-r--r--  1 timmy  staff    76M Jan 21 17:55 data.npy

>>> python npy_vs_msgpack.py
# Python 3.6 Result
input.shape:  (1000, 10000)
[WRITE MSGPACK]:  0.3175380229949951 sec(s)
[READ MSGPACK]:  0.04025006294250488 sec(s)
True
[WRITE NPY]:  0.09179878234863281 sec(s)
[READ NPY]:  0.030505895614624023 sec(s)
True
>>> ls -lh
-rw-r--r--  1 timmy  staff    86M Jan 21 17:54 data.msgpack
-rw-r--r--  1 timmy  staff    76M Jan 21 17:55 data.npy
~~~~

# Conclusion

1. Reading *.npy is slightly faster than *.msgpack

2. Writing *.npy is extremely faster than *.msgpack

3. *.npy is smaller than *.msgpack
