import json

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

# Adding s1 flows
s1_flows=[json_data_creator(id=1, table_id=0, priority=1, match={"ethernet-match":{"ethernet-type":{"type":0x806}}}, actions=[{"order":0, "output-action":{"output-node-connector":"FLOOD"}}])]
s1_flows.append(json_data_creator(id=2, table_id=0, priority=10, match={"ethernet-match":{"ethernet-type":{"type":0x800}, "ethernet-destination":{"address":"00:00:00:00:00:02"}}}, actions=[{"order":0, "output-action":{"output-node-connector":"2"}}]))
s1_flows.append(json_data_creator(id=3, table_id=0, priority=10, match={"ethernet-match":{"ethernet-type":{"type":0x800}, "ethernet-destination":{"address":"00:00:00:00:00:01"}}}, actions=[{"order":0, "output-action":{"output-node-connector":"1"}}]))

with open("./flows-json/s1-flows/s1-1.json", "w") as s1_1:
    json.dump(s1_flows[0], s1_1, indent=4)

with open("./flows-json/s1-flows/s1-2.json", "w") as s1_2:
    json.dump(s1_flows[1], s1_2, indent=4)

with open("./flows-json/s1-flows/s1-3.json", "w") as s1_3:
    json.dump(s1_flows[2], s1_3, indent=4)


# Adding s2 flows
s2_flows=[json_data_creator(id=1, table_id=0, priority=1, match={"ethernet-match":{"ethernet-type":{"type":0x806}}}, actions=[{"order":0, "output-action":{"output-node-connector":"FLOOD"}}])]
s2_flows.append(json_data_creator(id=2, table_id=0, priority=10, match={"ethernet-match":{"ethernet-type":{"type":0x800}, "ethernet-destination":{"address":"00:00:00:00:00:01"}}}, actions=[{"order":0, "output-action":{"output-node-connector":"2"}}]))
s2_flows.append(json_data_creator(id=3, table_id=0, priority=10, match={"ethernet-match":{"ethernet-type":{"type":0x800}, "ethernet-destination":{"address":"00:00:00:00:00:02"}}}, actions=[{"order":0, "output-action":{"output-node-connector":"1"}}]))

with open("./flows-json/s2-flows/s2-1.json", "w") as s2_1:
    json.dump(s2_flows[0], s2_1, indent=4)

with open("./flows-json/s2-flows/s2-2.json", "w") as s2_2:
    json.dump(s2_flows[1], s2_2, indent=4)

with open("./flows-json/s2-flows/s2-3.json", "w") as s2_3:
    json.dump(s2_flows[2], s2_3, indent=4)

# Adding r1 flows
s3_flows=[json_data_creator(id=1, table_id=0, priority=1, match={"ethernet-match":{"ethernet-type":{"type":0x806}}}, actions=[{"order":0, "output-action":{"output-node-connector":"FLOOD"}}])]
s3_flows.append(json_data_creator(id=2, table_id=0, priority=10, match={"ipv4-destination":"10.0.1.1/32", "ethernet-match":{"ethernet-type":{"type":0x800}}}, actions=[{"order":0, "dec-nw-ttl": {}}, {"order":1, "output-action":{"output-node-connector":"1"}}], order=2))
s3_flows.append(json_data_creator(id=3, table_id=0, priority=10, match={"ipv4-destination":"10.0.2.1/32", "ethernet-match":{"ethernet-type":{"type":0x800}}}, actions=[{"order":0, "dec-nw-ttl": {}}, {"order":1, "output-action":{"output-node-connector":"2"}}], order=2))

with open("./flows-json/s3-flows/s3-1.json", "w") as s3_1:
    json.dump(s3_flows[0], s3_1, indent=4)

with open("./flows-json/s3-flows/s3-2.json", "w") as s3_2:
    json.dump(s3_flows[1], s3_2, indent=4)

with open("./flows-json/s3-flows/s3-3.json", "w") as s3_3:
    json.dump(s3_flows[2], s3_3, indent=4)


