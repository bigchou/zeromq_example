~~~~
# [JSON] Python 3.6 v.s. Python 2.7
(zeromq_py2) timmy@WANs-MacBook-Pro-2 time_test % python json_server.py
(zeromq) timmy@WANs-MacBook-Pro-2 time_test % python json_client.py    
object size: 2724993
RECEIVE RESPONSE FROM SERVER
MY_RESPONSE
time elapsed: 0.41770195960998535

# [MSGPACK] Python 3.6 v.s. Python 2.7
(zeromq_py2) timmy@WANs-MacBook-Pro-2 time_test % python msgpack_server.py
(zeromq) timmy@WANs-MacBook-Pro-2 time_test % python msgpack_client.py 
object size: 518503
RECEIVE RESPONSE FROM SERVER
MY_RESPONSE
time elapsed: 0.0073947906494140625

# [JSON] Python 3.6 v.s. Python 3.6
(zeromq) timmy@WANs-MacBook-Pro-2 time_test % python json_server.py
(zeromq) timmy@WANs-MacBook-Pro-2 time_test % python json_client.py 
object size: 2724993
RECEIVE RESPONSE FROM SERVER
MY_RESPONSE
time elapsed: 0.19679689407348633

# [MSGPACK] Python 3.6 v.s. Python 3.6
(zeromq) timmy@WANs-MacBook-Pro-2 time_test % python msgpack_server.py
(zeromq) timmy@WANs-MacBook-Pro-2 time_test % python msgpack_client.py 
object size: 518503
RECEIVE RESPONSE FROM SERVER
MY_RESPONSE
time elapsed: 0.006613016128540039
~~~~

# Conclusion
About transmission, using msgpack is time-efficient and space-efficient.
