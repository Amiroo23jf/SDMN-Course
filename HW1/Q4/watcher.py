import os
import json
import shutil
from xmlrpc.client import Boolean
import numpy as np
import requests 
from requests.auth import HTTPBasicAuth
import time
import spf
import create_flows
import send_flows


def link_states():
    '''returns the state of links as a matrix containig zeros and ones'''
    url = "http://localhost:8181/restconf/operational/opendaylight-inventory:nodes"
    response = requests.get(url, auth=HTTPBasicAuth('admin', 'admin'))
    try:
        n = len(response.json()["nodes"]["node"])
    except:
        return None
    link_states = np.zeros((n, n)).astype("int8")
    for node in response.json()["nodes"]["node"]:
        node_id = int(node["id"].split(":")[1])
        for connector in node["node-connector"]:
            port_name = connector["id"].split(":")[2]
            intf_name = connector["flow-node-inventory:name"]
            link_state = not(connector["flow-node-inventory:state"]["link-down"])
            if (port_name == "LOCAL"):
                continue
            node_out = int(intf_name.split('-')[1][3:])
            if (link_state == True):
                link_states[node_id-1][node_out-1] = 1
    return link_states
    
def check_net_state():
    '''checks the file is_up.json and checks if the mininet network is still up or not'''
    with open("data/is_up.json", "r") as f:
        is_up = bool(f.read())
    return is_up


with open('data/A.json', 'r') as f1:
    A = np.array(json.load(f1))

spf_1_n, spf_n_1 = spf.spf(A)


A_previous = A.copy()
is_up = check_net_state()
t=time.time()
while is_up :
    while(time.time() - t < 5):
        continue
    
    # Ends the while if the mininet network is not up
    is_up = check_net_state()
    #print("Network is up:", is_up)
    if (is_up == False):
        continue
    t = time.time()
    link_states_arr = link_states()

    if type(link_states_arr) == type(None):
        break
    A_new = A * link_states_arr
    # finding the new shortest path
    spf_1_n_new, spf_n_1_new= spf.spf(A_new)

    # check if the network state is changed or not (In order to prevent unnecessary flows)
    if ((spf_1_n_new == spf_1_n) and (spf_n_1_new == spf_n_1)):
        continue
    
    spf_1_n = spf_1_n_new
    spf_n_1 = spf_n_1_new

    print("The network links are changed!")
    print("Updating the flows...")
    A_previous = A_new.copy()
    
    # removing the files and subdirectories in the 'flows-json' directory
    path = 'flows-json'
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        


    print("New shortest path from 1 to n:", spf_1_n)
    print("New shortest path from n to n:", spf_n_1)

    # creating and sending the new flows
    create_flows.flow_creator(load_from_file=False, A=A_new.copy(), spf_1_n=spf_1_n.copy(), spf_n_1=spf_n_1.copy())
    send_flows.send_flows(remove_previous=True)

    print("The flows are successfully updated!"+"\n")

    
print("Watcher is shut down.")
