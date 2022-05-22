# adding tunnel id to flows
ovs-ofctl add-flow s1 table=0,in_port=s1-eth1,actions=set_field:100-\>tunnel_id,output:vxlan1
ovs-ofctl add-flow s1 table=0,in_port=s1-eth2,actions=set_field:200-\>tunnel_id,output:vxlan1

# recieved by vxlan port
ovs-ofctl add-flow s1 table=0,in_port=vxlan1,tunnel_id=100,actions=output:s1-eth1
ovs-ofctl add-flow s1 table=0,in_port=vxlan1,tunnel_id=200,actions=output:s1-eth2



