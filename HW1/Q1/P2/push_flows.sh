# Adding s1 flows
ovs-ofctl add-flow s1 priority=1,arp,actions=flood
ovs-ofctl add-flow s1 priority=10,ip,dl_dst=00:00:00:00:00:02,actions=output:2
ovs-ofctl add-flow s1 priority=10,ip,dl_dst=00:00:00:00:00:01,actions=output:1

# Adding s2 flows
ovs-ofctl add-flow s2 priority=1,arp,actions=flood
ovs-ofctl add-flow s2 priority=10,ip,dl_dst=00:00:00:00:00:01,actions=output:2
ovs-ofctl add-flow s2 priority=10,ip,dl_dst=00:00:00:00:00:02,actions=output:1

# Adding r1 flows
ovs-ofctl add-flow r1 priority=1,arp,actions=flood
ovs-ofctl add-flow r1 priority=10,ip,nw_dst=10.0.1.0/24,actions=dec_ttl,output:1
ovs-ofctl add-flow r1 priority=10,ip,nw_dst=10.0.2.0/24,actions=dec_ttl,output:2

