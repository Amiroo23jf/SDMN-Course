import requests
from requests.auth import HTTPBasicAuth

def push_flow(node, table_id, id, flow_addr, c_ip = 'localhost:8181'):
    '''This function gets the a node (eg. openflow:1), a table_id, an id (which is the flow id), a flow_addr containing the flow's json address and the controller's ip:port
       and sends a put request containing the given information to the controller'''
    url = 'http://'+c_ip+'/restconf/config/opendaylight-inventory:nodes/node/'+node+'/flow-node-inventory:table/'+table_id+'/flow/'+id
    headers = {"Content-Type": "application/json"}
    with open(flow_addr, 'r') as data_file:
        data = data_file.read()
        response = requests.put(url, data=data, headers=headers, auth=HTTPBasicAuth('admin','admin'))
    return

for i in range(1,4): # i = switch number
    for j in range(1,4): # j = flow number
        push_flow(node="openflow:"+str(i) , table_id="0", id=str(j), flow_addr="./flows-json/s"+str(i)+"-flows/s"+str(i)+"-"+str(j)+".json" )
