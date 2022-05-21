import shutil
import requests
import os
from requests.auth import HTTPBasicAuth

url = "http://localhost:8181/restconf/config/opendaylight-inventory:nodes"
response = requests.delete(url, auth=HTTPBasicAuth('admin','admin'))
print("Controller Flows are successfully deleted!")

if os.path.isdir('data'):
    shutil.rmtree('data')
    print("Data Directory is successfully deleted!")
if os.path.isdir('flows-json'):
    shutil.rmtree('flows-json')
    print("Flow jsons are successfully deleted!")

