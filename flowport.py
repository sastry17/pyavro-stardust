#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 03:51:43 2021

@author: sastry17
"""

# Example code that uses the AvroFlowtuple3Reader extension class to
# count flowtuples via a perFlowtuple callback method

import sys
from collections import defaultdict
from pyavro_stardust.flowtuple3 import AvroFlowtuple3Reader, \
        Flowtuple3AttributeNum, Flowtuple3AttributeStr


# Incredibly simple callback that simply increments a global counter for
# each flowtuple, as well as tracking the number of packets for each
# IP protocols
def perFlowtupleCallback(ft, userarg):
    #global counter, protocols
    #counter += 1
    f = open('01042021.csv','a')

    a = ft.asDict()

    #check records for destination port of IoT protocols
    if a["dst_port"]==1883 or a["dst_port"]==5672  or a["dst_port"]== 5683 \
    or a["dst_port"]== 1900 or a["dst_port"]== 5269 or a["dst_port"]== 23:
        ipint = a["src_ip"]
        ip = ""
        for i in range(4):
            ip1 = ""
            for j in range(8):
                #print (ipint % 2)
                ip1=str(ipint % 2)+ip1
                ipint = ipint >> 1
                #print (ip1)
            print (ip1)
            ip = str(int(ip1,2)) + "." + ip
        print(ip.strip(".")+":"+str(a["dst_port"]))
        ip = ip.strip(".")
        port = a["dst_port"]
        timestamp = a["timestamp"]
        record = "\n"+ip+","+port+","+timestamp
        f.write(record)
        
        
        
    
 
def run():

    # sys.argv[1] must be a valid wandio path -- e.g. a swift URL or
    # a path to a file on disk
    ftreader = AvroFlowtuple3Reader(sys.argv[1])
    ftreader.start()

    # This will read all flowtuples and call `perFlowtupleCallback` on
    # each one
    ftreader.perAvroRecord(perFlowtupleCallback)

    ftreader.close()

  

run()