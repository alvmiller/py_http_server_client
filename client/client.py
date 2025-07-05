#!/usr/bin/env python  

import http.client
import sys  
import time
import socket
import requests
  
#get http server ip  
http_server = sys.argv[1]  
sleep_var = sys.argv[2]
  
print("http_server: ", http_server) 
print("sleep_var: ", sleep_var) 

count = 0
while 1:  
  try:
    print("count: ", count) 

    headers = {
      "User-Agent": "MyApp/1.0",
      "Authorization": "Bearer your_token_here"
    }
    # Send a GET request
    response = requests.get("http://" + http_server)
    print("Response text:", response.text)
    # Get the response
    # Print the response status code and reason
    print(f"Status Code: {response.status_code}")
    print(f"Reason: {response.reason}")
    if response.status_code == 200:
      print("Request was successful")
    elif response.status_code == 404:
      print("Resource not found")
      break
    else:
      print("Unexpected status code:", response.status_code)
      break
    print()
    time.sleep(float(sleep_var)) 

  except http.client.HTTPException as e:
    print("HTTP Exception:", e)
  except Exception as e:
    print("An error occurred:", e)
  finally:
    count = count + 1
    if count == 5:
      break
    time.sleep(float(sleep_var))  
