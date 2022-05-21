import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8181/restconf/config/opendaylight-inventory:nodes"
response = requests.delete(url, auth=HTTPBasicAuth('admin','admin'))
print("Controller Flows are successfully deleted!")
