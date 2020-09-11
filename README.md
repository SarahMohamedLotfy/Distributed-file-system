# Distributed-file-system-using-python-ZMQ-for-communication-between-processes
Distributed-file-system-using-python-ZMQ-for-communication-between-processes

TYDFS is a centralized distributed system. TYDFS has 2 types of machine
nodes. First, the Master Tracker node. This node has a look-up table. The
look-up table columns are (user id, file name, data node number, file path on
that data node, is data node alive). We will assume the all the files will be
mp4 files. Second, the Data Keeper nodes. Data Keeper nodes are the actual
nodes that have the data files.

![7](https://user-images.githubusercontent.com/48661473/92958290-d18b8780-f41e-11ea-9e04-5bc3ac53b7e7.JPG)

![1](https://user-images.githubusercontent.com/48661473/92957938-3db9bb80-f41e-11ea-8dab-9576b253ae82.jpg)

![2](https://user-images.githubusercontent.com/48661473/92958041-6772e280-f41e-11ea-9d75-1f2d61c59cf5.jpg)

![3](https://user-images.githubusercontent.com/48661473/92958100-7e193980-f41e-11ea-8863-ec8afb5fcd0f.jpg)

![4](https://user-images.githubusercontent.com/48661473/92958154-938e6380-f41e-11ea-8c50-82ec6d05b513.jpg)

![5](https://user-images.githubusercontent.com/48661473/92958205-a7d26080-f41e-11ea-9f35-d8446024fc21.jpg)

![6](https://user-images.githubusercontent.com/48661473/92958255-bfa9e480-f41e-11ea-81a3-c9cd5c50adb0.JPG)
