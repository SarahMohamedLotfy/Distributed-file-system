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
import numpy as np
from multiprocessing import Process, Manager


 
def processALive():
   
   ctx = zmq.Context()
   sock = ctx.socket(zmq.SUB)
   sock.connect("tcp://127.0.0.1:6001")
   sock.subscribe("") # Subscribe to all topics

   print("Starting receiver loop ...")
   while True:
    msg = sock.recv_string()
    #print("Received string: %s ..." % msg)

   sock.close()
   ctx.term()



    
def masterp (i,dataKeeperPorts):
    
    context = zmq.Context()
    masterr_recv = context.socket(zmq.PAIR)
    masterr_recv.connect("tcp://127.0.0.1:%s"%(i))
    
    which = masterr_recv.recv_json()
   
    print ("Master receiving from client")
    upDown= which ['what']
    FileName= which['namefile']
    masterr_recv.close()
    if upDown == "download":
          
        if len(dataKeeperPorts) !=0:
          
          portwilused = dataKeeperPorts[0]
          del dataKeeperPorts[0]
         
          print ("Port will be used",portwilused)
          context = zmq.Context()
          master_sender = context.socket(zmq.PAIR)
          master_sender.bind("tcp://127.0.0.1:%s"%(i))
 
          master_sender.send_string(portwilused)
          print ("master sent port to client")
          master_sender.close()
          
          print (dataKeeperPorts)
          dataKeeperPorts.append(portwilused)

        else:
         
            msg= "there is no available port"
            print (msg)
            context = zmq.Context()
            master_sender = context.socket(zmq.PAIR)
            master_sender.bind("tcp://127.0.0.1:%s"%(i))
 
            master_sender.send_string(msg)
            print ("Master sent port to client")
            master_sender.close()
           

    else:
       
       #Upload
        
        if len(dataKeeperPorts) !=0:
          
          portwilused = dataKeeperPorts[0]
          del dataKeeperPorts[0]
          
          print ("Port will be used upload",portwilused)
          context = zmq.Context()
          master_sender = context.socket(zmq.PAIR)
          master_sender.bind("tcp://127.0.0.1:%s"%(i))
 
          master_sender.send(portwilused)
          print ("Master sent port to client")
          master_sender.close()
         
       
         # master receive notify from datakeeper that uploading finsihed
          masterport = 6000
          contex = zmq.Context()
          dataMaster = contex.socket(zmq.PAIR)
          dataMaster.connect("tcp://127.0.0.1:%s"%(masterport))
          notify = dataMaster.recv_json()
          #dataKeeprpoertscheck [result[0]] = 1
          
          print (dataKeeperPorts)
          msg = notify['msg']
          portused = notify ['portused']
          print(msg)
          print (portused)
          dataMaster.close()
          
          dataKeeperPorts.append(portwilused)
          
        else:
         
            msg= "there is no available port"
            print (msg)
            context = zmq.Context()
            master_sender = context.socket(zmq.PAIR)
            master_sender.bind("tcp://127.0.0.1:%s"%(i))
 
            master_sender.send_string(msg)
            print ("Master sent port to client")
            master_sender.close()
         
        
        


if __name__=='__main__':
   
   port1 = 5310
   port2 = 5314
   port3=  5316

   manager = Manager() 
           
   dataKeeperPorts = manager.list()
   dataKeeperPorts.append("5156")
   dataKeeperPorts.append("5710")
   dataKeeperPorts.append("5687")
    
   p1 = Process(target=masterp, args=(port1,dataKeeperPorts,)) 
   p2 = Process(target=masterp, args=(port2,dataKeeperPorts,)) 
   p3 = Process(target=masterp, args=(port3,dataKeeperPorts,)) 
   p4 = multiprocessing.Process(target=processALive)
    
   p1.start() 
  # time.sleep(10)
   print ("hwa")
   print (dataKeeperPorts)
   p2.start() 
   p3.start() 
   p4.start()
   

   p1.join() 
   p2.join() 
   p3.join()
   p4.join()
    
   print("Done!") 
  
