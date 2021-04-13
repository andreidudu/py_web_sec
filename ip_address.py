#!/bin/python3
 
import os
import re

def get_ip_address(url):
 	command = "host " + url[8:]
 	print ('url = ', url[8:])
 	process = os.popen(command)
 	results = str(process.read())
 	print (process)
 	marker = re.search(r'has address(.*)', results)
 	print (marker)
 	return results
 	

