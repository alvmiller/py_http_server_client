#!/usr/bin/env python  

import http.server
import requests
import os 
import re 

#import pymysql
import json
import logging

def get_server_address():
  return '127.0.0.1'

def get_server_port():
  return 80

def get_rootdir():
  return 'server/html/'
  
class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
  #handle GET command  
  def do_GET(self):
    print()
    print("GET...")
    print("self:", self)
    get_file = "dummy.html"
    full_file = get_rootdir() + get_file
    try:
      print("self.path: ", self.path)
      print ('Needed file: ', full_file)
      f = open(full_file) #open requested file 
      #send code 200 response  
      self.send_response(200)  
      #send header first  
      self.send_header('Content-type','text-html')  
      self.end_headers()  
      #send file content to client  
      print("555")  
      data = json.dumps(f.read()).encode('utf-8')
      self.wfile.write(data)
      #self.wfile.write(f.read())  
      print("666")  
      f.close()  
      return

    except IOError as err:  
      print("IOError catched", err)
      self.send_error(404, 'file not found') 
    except Exception as e:
      print("Something else went wrong:", e)
    finally:
      print("The 'try except' is finished")

def logs():
  logger = logging.getLogger(__name__)
  logging.basicConfig(filename='myapp.log', level=logging.INFO)
  logger.info('Started')
  logger.info('Finished')

def jsons_db():
  dictionary = {
    "app": "server"
  }
  # Serializing json
  json_object = json.dumps(dictionary, indent=4)
  # Writing to sample.json
  with open("sample.json", "w") as outfile:
    outfile.write(json_object)

def sqlite_db():
  TBD

def mongodb_db():
  TBD

def run():  
  print('http server is starting...') 

  logs()
  jsons_db()
  
  #ip and port of servr  
  #by default http server port is 80  
  server_address = (get_server_address(), get_server_port())  
  httpd = http.server.HTTPServer(server_address, HTTPRequestHandler)  
  print('http server is running...')  
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  logging.info('Stopping httpd...\n')
  httpd.server_close()

if __name__ == '__main__': 
  run()  
