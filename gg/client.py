
import time
import zmq
import pprint
import sys

def client(k,filenamee,upordownload):
  
  #j = 5156
  #i = 5310
  i = int (k)
  #Client request from Master
  context = zmq.Context()
  client_req = context.socket(zmq.PAIR)
  client_req.bind("tcp://127.0.0.1:%s"%(i))
  download = {'what':upordownload,'namefile':'sample.mp4'}
  client_req.send_json(download)
  print ("Client request from master")
    
  client_req.close()

  #Client receive port from master
  context = zmq.Context()
  c_receiver = context.socket(zmq.PAIR)
  c_receiver.connect("tcp://127.0.0.1:%s"%(i))

  data = c_receiver.recv()
  j = int (data)
  print (j)

#Client request downloading from datakeeper

  context = zmq.Context()
  client_sender = context.socket(zmq.PAIR)
  client_sender.bind("tcp://127.0.0.1:%s"%(j))
  upordown = {'what':upordownload,'namefile':filenamee}
  client_sender.send_json(upordown)
  print ("Client request from Datakeeper")
     
  client_sender.close()
  ud = upordownload
  
  if ud== "download":
    
    context = zmq.Context()
    results_receiver = context.socket(zmq.PAIR)
    results_receiver.connect("tcp://127.0.0.1:%s"%(j))

    filen= "maa"
    with open(filenamee, 'wb') as f:
      print 'file opened'
       
      print('receiving data...')
      data = results_receiver.recv()
      # write data to a file
      f.write(data)
    f.close()
    print('client Successfully get the file')
   #results_receiver.close()
    print('connection closed')
  else:
    time.sleep(10)
    client_sender.close()

    
    #Upload
    context = zmq.Context()
    cl_sender = context.socket(zmq.PAIR)
    cl_sender.bind("tcp://127.0.0.1:%s"%(j))
    f = open(filenamee,'rb')
    l = f.read()
       
    cl_sender.send(l)
    f.close()
    print('Client send file to Data keeper ( Upload)')
    cl_sender.close()
client(sys.argv[1],sys.argv[2], sys.argv[3])
 
