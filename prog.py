import requests
import time
import json
import sys
import imp
imp.reload(sys)

url='http://35.189.233.152'

for i in range(100):
    r = requests.get(url)
    print(i,r)


