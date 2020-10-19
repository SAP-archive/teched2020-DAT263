import requests
import argparse
import random

from datetime import datetime

# DI pipeline path: DI-URL/<path>/<operation>
url = 'https://vsystem.ingress.dh-ia37o5zq.dhaas-live.shoot.live.k8s-hana.ondemand.com/app/pipeline-modeler/openapi/service/teched2020/performance/data'

# commandline parser
parser = argparse.ArgumentParser(description='Sending device data to SAP Data Intelligence.')
parser.add_argument('--cellid', type = int, help = "device identifier")
parser.add_argument('--user',  type = str ,help = "user")
parser.add_argument('--pwd',  type = str , help = "password")
args = parser.parse_args()

# data creation
key1 = random.gauss(100,10)
key2 = random.gauss(200,20)
data = {'TIMESTAMP': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'CELLID': args.cellid, 'KEY1':key1, 'KEY2':key2}

# send request
auth = ('default\\' + args.user,args.pwd)
headers = {'X-Requested-With': 'XMLHttpRequest'}
resp = requests.post(url, json = data,auth=auth,headers=headers)

# response
print(resp)