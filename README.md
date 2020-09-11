# Distributed-file-system-using-python-ZMQ-for-communication-between-processes
Distributed-file-system-using-python-ZMQ-for-communication-between-processes

TYDFS is a centralized distributed system. TYDFS has 2 types of machine
nodes. First, the Master Tracker node. This node has a look-up table. The
look-up table columns are (user id, file name, data node number, file path on
that data node, is data node alive). We will assume the all the files will be
mp4 files. Second, the Data Keeper nodes. Data Keeper nodes are the actual
nodes that have the data files.


