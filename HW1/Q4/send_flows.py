import requests
from requests.auth import HTTPBasicAuth
import os

def push_flow(node, table_id, id, flow_addr, c_ip = 'localhost:8181'):
    '''This function gets the a node (eg. openflow:1), a table_id, an id (which is the flow id), a flow_addr containing the flow's json address and the controller's ip:port
       and sends a put request containing the given information to the controller'''
    url = 'http://'+c_ip+'/restconf/config/opendaylight-inventory:nodes/node/'+node+'/flow-node-inventory:table/'+table_id+'/flow/'+id
    headers = {"Content-Type": "application/json"}
    with open(flow_addr, 'r') as data_file:
        data = data_file.read()
        response = requests.put(url, data=data, headers=headers, auth=HTTPBasicAuth('admin','admin'))
    return

def send_flows(c_ip='localhost:8181', remove_previous=False):
    if remove_previous:
        url = 'http://'+c_ip+'/restconf/config/opendaylight-inventory:nodes'
        requests.delete(url, auth=HTTPBasicAuth('admin','admin'))
    flows_dir = 'flows-json'
    switch_dirs = os.listdir(flows_dir)
    node_ids = list(map(lambda x: int(x.split('-')[0][1:]), switch_dirs))
    n = len(node_ids)
    for i in range(n):
        node_id = node_ids[i]
        s_dir = os.path.join(flows_dir, switch_dirs[i])
        s_flows = os.listdir(s_dir)
        flow_addrs = list(map(lambda x: os.path.join(s_dir, x), s_flows))
        flow_ids = list(map(lambda x: x.split('.')[0][4:], s_flows))
        m = len(flow_ids)
        for j in range(m):
            addr = flow_addrs[j]
            id = flow_ids[j]
            node = "openflow:"+str(node_id)
            push_flow(node=node , table_id="0", id=id, flow_addr=addr)

if __name__=="__main__":
    send_flows()
