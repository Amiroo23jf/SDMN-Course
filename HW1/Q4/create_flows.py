import json
import os
import numpy as np

def json_data_creator(id, table_id, priority, match, actions, idle_timeout=None, order=0):
    '''This function, creates the json of the flow by getting the properties of a flow as the input.'''
    data_dict = {"id": str(id)}
    data_dict["table_id"] = table_id
    data_dict["flow-name"] = "flow"+str(id)
    data_dict["priority"] = priority
    data_dict["match"] = match
    data_dict["instructions"] = {"instruction":[{"order":order, "apply-actions":{"action":actions}}]}
    if idle_timeout != None:
        data_dict["idle-timeout"] = idle_timeout
    return {"flow-node-inventory:flow":[data_dict]}

def flow_creator(load_from_file = True, A = None, spf_1_n = None, spf_n_1 = None):
    '''This function takes A, shortest path from 1 to n (spf_1_n) and from n to 1 (spft_n_1) and creates the related json files.'''

    # loading files
    if load_from_file:
        with open('data/A.json', 'r') as f1:
            A = np.array(json.load(f1))
        with open('data/spf_1_n.json', 'r') as f2:
            spf_1_n = json.load(f2)
        with open('data/spf_n_1.json', 'r') as f3:
            spf_n_1 = json.load(f3)
    with open('data/port_intf_dict.json', 'r') as f4:
        port_intf_dict = json.load(f4)

    # creating the 'flows-json' directory in order to store flows
    try:
        os.makedirs("flows-json", mode=0o777)
    except OSError as error:
        pass
    n = A.shape[0]

    # creating directory corresponding to each node inside the 'flows-json' directory
    for i in range(1, n+1):
        try:
            os.mkdir("flows-json/s"+str(i)+"-flows")
        except OSError as error:
            pass
    node_flow_id = [1] * n # contains the current available flow-id for each node

    # adding flows for the path from 1 to n
    s_previous = spf_1_n[0]
    while len(spf_1_n)>=1:
        s = spf_1_n.pop(0)
        id = node_flow_id[s-1]
        node_flow_id[s-1] += 1
        if (len(spf_1_n)!=0):
            s_next = spf_1_n[0]
        else:
            s_next = s
        in_port = port_intf_dict["s"+str(s)+"-eth"+str(s_previous)]
        out_port = port_intf_dict["s"+str(s)+"-eth"+str(s_next)]
        flow_dict = json_data_creator(id=id, table_id=0, priority=10, match={"in-port": str(in_port),
         "arp-target-transport-address": "10.0.2.1/32", "ethernet-match":{"ethernet-type":{"type": 0x806}}},
          actions=[{"order":0, "output-action":{"output-node-connector":str(out_port)}}])
        with open("./flows-json/s"+str(s)+"-flows/flow"+str(id)+".json", "w") as flow_file:
            json.dump(flow_dict, flow_file, indent=4)

        id = node_flow_id[s-1]
        node_flow_id[s-1] += 1
        flow_dict = json_data_creator(id=id, table_id=0, priority=10, match={"in-port": str(in_port),
         "ipv4-destination": "10.0.2.1/32", "ethernet-match":{"ethernet-type":{"type": 0x800}}},
          actions=[{"order":0, "output-action":{"output-node-connector":str(out_port)}}])
        with open("./flows-json/s"+str(s)+"-flows/flow"+str(id)+".json", "w") as flow_file:
            json.dump(flow_dict, flow_file, indent=4)
        s_previous = s

    # adding flows for the path from n to 1
    s_previous = spf_n_1[0]
    while len(spf_n_1)>=1:
        s = spf_n_1.pop(0)
        id = node_flow_id[s-1]
        node_flow_id[s-1] += 1
        if (len(spf_n_1)!=0):
            s_next = spf_n_1[0]
        else:
            s_next = s
        in_port = port_intf_dict["s"+str(s)+"-eth"+str(s_previous)]
        out_port = port_intf_dict["s"+str(s)+"-eth"+str(s_next)]
        flow_dict = json_data_creator(id=id, table_id=0, priority=10, match={"in-port": str(in_port),
         "arp-target-transport-address": "10.0.1.1/32", "ethernet-match":{"ethernet-type":{"type": 0x806}}},
          actions=[{"order":0, "output-action":{"output-node-connector":str(out_port)}}])
        with open("./flows-json/s"+str(s)+"-flows/flow"+str(id)+".json", "w") as flow_file:
            json.dump(flow_dict, flow_file, indent=4)

        id = node_flow_id[s-1]
        node_flow_id[s-1] += 1
        flow_dict = json_data_creator(id=id, table_id=0, priority=10, match={"in-port": str(in_port),
         "ipv4-destination": "10.0.1.1/32", "ethernet-match":{"ethernet-type":{"type": 0x800}}},
          actions=[{"order":0, "output-action":{"output-node-connector":str(out_port)}}])
        with open("./flows-json/s"+str(s)+"-flows/flow"+str(id)+".json", "w") as flow_file:
            json.dump(flow_dict, flow_file, indent=4)
        s_previous = s

if __name__ =='__main__':
    flow_creator()
