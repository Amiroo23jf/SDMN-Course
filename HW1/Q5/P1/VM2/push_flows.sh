# adding tunnel id to flows
ovs-ofctl add-flow s2 table=0,in_port=s2-eth1,actions=set_field:100-\>tunnel_id,output:vxlan2
ovs-ofctl add-flow s2 table=0,in_port=s2-eth2,actions=set_field:200-\>tunnel_id,output:vxlan2

# received by vxlan port
ovs-ofctl add-flow s2 table=0,in_port=vxlan2,tunnel_id=100,actions=output:s2-eth1
ovs-ofctl add-flow s2 table=0,in_port=vxlan2,tunnel_id=200,actions=output:s2-eth2
