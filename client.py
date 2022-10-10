import sys
import json
import requests
'''n=input()
data=json.dumps(n)
resp={
      "Response":200,
      "Message":"data from python to node js",
      "Data":data
      }
print(json.dumps(resp))
print("Hello")
sys.stdout.flush()'''
n=sys.argv[1]
print(n)
