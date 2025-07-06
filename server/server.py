#!/usr/bin/env python  

import http.server
import requests
import os 
import re 

#import pymysql
import json
import logging
import sqlite3
#import pymongo

def get_server_address():
  return '127.0.0.1'

def get_server_port():
  return 8080

def get_rootdir():
  return 'html/'
  
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
  try:
    with sqlite3.connect("my.db") as conn:
      # interact with database
      print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
      pass
  except sqlite3.OperationalError as e:
    print("Failed to open database:", e)

def mongodb_db():
  #myclient = pymongo.MongoClient("mongodb://localhost:27017/")
  #mydb = myclient["mydatabase"]
  return

def run():  
  print('http server is starting...') 

  logs()
  jsons_db()
  sqlite_db()
  mongodb_db()
  
  #ip and port of servr  
  #by default http server port is 8080  
  server_address = (get_server_address(), get_server_port())  
  httpd = http.server.HTTPServer(server_address, HTTPRequestHandler)  
  print('get_server_address: ', get_server_address())  
  print('get_server_port:', get_server_port())  
  print('http server is running...')  
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  logging.info('Stopping httpd...\n')
  httpd.server_close()

if __name__ == '__main__': 
  run()  
