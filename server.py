import time
import zmq
import time
import zmq
import pprint
import time
import zmq
import time
import zmq
import pprint
import sys
import shutil
import os
import cv2
import multiprocessing 
import random

  

def dataKeeperProcess(port):
    
    #Data keeper node receive from master which to download or upload

    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://127.0.0.1:%s"%(port))
    upORdown = socket.recv_json()
    time.sleep(10)
    socket.close()
    upDown= upORdown ['what']
    FileName= upORdown['namefile']
    print (FileName)
    print (upDown)
    
    if upDown !="download":
      context = zmq.Context()
      socket = context.socket(zmq.PAIR)
      socket.connect("tcp://127.0.0.1:%s"%(port))
    
      
      with open(FileName, 'wb') as f:
        print 'file opened'
        print('receiving data...')
        data = socket.recv()
      
        # write data to a file
        f.write(data)
      f.close()


      print('Data keeper Successfully get the file')
      socket.close()
      print('connection closed')

      #DataKeeper notify master that uploading finished
      masterport = 6000
      contex = zmq.Context()
      dataMaster = contex.socket(zmq.PAIR)
      dataMaster.bind("tcp://127.0.0.1:%s"%(masterport))
      notify = {'msg':"Uploading finished",'portused': port }
      dataMaster.send_json(notify)
      print("DataKeeper notify master that uploading finished")
      dataMaster.close()

    else:
        context = zmq.Context()
        
        data_sender = context.socket(zmq.PAIR)
        #data_sender.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      
        data_sender.bind("tcp://127.0.0.1:%s"%(port))
    
        f = open(FileName,'rb')
        l = f.read()
       
        data_sender.send(l)
        f.close()
  
        print('Data keeper send file to client ( Download)')
        data_sender.close()

        


def aliveprocess(port):
  
   ctx = zmq.Context()
   sock = ctx.socket(zmq.PUB)
   sock.bind("tcp://*:%s"%(port))

   while True:
       msg = "I am Alive" 
       sock.send_string(msg)
       #print("Sent string: %s ..." % msg)
       

   sock.close()
   ctx.term()

if __name__=='__main__':
   port1 = 5156
   port2 = 5710
   port3=  5687
   portBetDataMaster= 6001
   p1 = multiprocessing.Process(target=dataKeeperProcess, args=(port1,)) 
   p2 = multiprocessing.Process(target=dataKeeperProcess, args=(port2,)) 
   p3 = multiprocessing.Process(target=dataKeeperProcess, args=(port3,)) 
   p4 = multiprocessing.Process(target=aliveprocess, args=(portBetDataMaster,))
    
   p1.start() 
   p2.start() 
   p3.start() 
   p4.start()
    
   p1.join() 
   p2.join() 
   p3.join()
   p4.join()

   print("Done!") 
   
