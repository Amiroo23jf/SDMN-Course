## we use mpls_tc field to divide arp and ipv4 requests. mpls_tc=0 for arp and mpls_tc=1 for ipv4

# Adding s1 flows
ovs-ofctl -O OpenFlow13 add-flow s1 in_port=s1-eth1,arp,actions=push_mpls:0x8847,set_field:12-\>mpls_label,set_field:0-\>mpls_tc,output:s1-eth2
ovs-ofctl -O OpenFlow13 add-flow s1 in_port=s1-eth1,ip,actions=push_mpls:0x8847,set_field:12-\>mpls_label,set_field:1-\>mpls_tc,output:s1-eth2
ovs-ofctl -O OpenFlow13 add-flow s1 in_port=s1-eth2,dl_type=0x8847,mpls_tc=0,mpls_label=21,actions=pop_mpls:0x0806,output:s1-eth1
ovs-ofctl -O OpenFlow13 add-flow s1 in_port=s1-eth2,dl_type=0x8847,mpls_tc=1,mpls_label=21,actions=pop_mpls:0x0800,output:s1-eth1


# Adding s2 flows

ovs-ofctl -O OpenFlow13 add-flow s2 table=0,in_port=s2-eth1,arp,nw_dst=10.0.0.1/32,actions=push_mpls:0x8847,set_field:21-\>mpls_label,set_field:0-\>mpls_tc,output=s2-eth2
ovs-ofctl -O OpenFlow13 add-flow s2 table=0,in_port=s2-eth1,arp,nw_dst=10.0.0.3/32,actions=push_mpls:0x8847,set_field:23-\>mpls_label,set_field:0-\>mpls_tc,output=s2-eth3
ovs-ofctl -O OpenFlow13 add-flow s2 table=0,in_port=s2-eth1,dl_type=0x0800,dl_dst=00:00:00:00:00:01,actions=push_mpls:0x8847,set_field:21-\>mpls_label,set_field:1-\>mpls_tc,output=s2-eth2
ovs-ofctl -O OpenFlow13 add-flow s2 table=0,in_port=s2-eth1,dl_type=0x0800,dl_dst=00:00:00:00:00:03,actions=push_mpls:0x8847,set_field:23-\>mpls_label,set_field:1-\>mpls_tc,output=s2-eth3

ovs-ofctl -O OpenFlow13 add-flow s2 table=0,in_port=s2-eth3,dl_type=0x8847,mpls_tc=1,dl_dst=00:00:00:00:00:01,actions=set_field:21-\>mpls_label,output:s2-eth2
ovs-ofctl -O OpenFlow13 add-flow s2 table=0,in_port=s2-eth2,dl_type=0x8847,mpls_tc=1,dl_dst=00:00:00:00:00:03,actions=set_field:23-\>mpls_label,output:s2-eth3

ovs-ofctl -O OpenFlow13 add-flow s2 table=0,dl_type=0x8847,mpls_tc=0,actions=pop_mpls:0x0806,goto_table=1
ovs-ofctl -O OpenFlow13 add-flow s2 table=0,dl_type=0x8847,mpls_tc=1,dl_dst=00:00:00:00:00:02,actions=pop_mpls:0x0800,output:s2-eth1

ovs-ofctl -O OpenFlow13 add-flow s2 table=1,arp,nw_dst=10.0.0.1/32,actions=push_mpls:0x8847,set_field:21-\>mpls_label,set_field:0-\>mpls_tc,output:s2-eth2
ovs-ofctl -O OpenFlow13 add-flow s2 table=1,arp,nw_dst=10.0.0.3/32,actions=push_mpls:0x8847,set_field:23-\>mpls_label,set_field:0-\>mpls_tc,output:s2-eth3
ovs-ofctl -O OpenFlow13 add-flow s2 table=1,arp,nw_dst=10.0.0.2/32,actions=output:s2-eth1

# Adding s3 flows
ovs-ofctl -O OpenFlow13 add-flow s3 in_port=s3-eth1,arp,actions=push_mpls:0x8847,set_field:32-\>mpls_label,set_field:0-\>mpls_tc,output:s3-eth2
ovs-ofctl -O OpenFlow13 add-flow s3 in_port=s3-eth1,ip,actions=push_mpls:0x8847,set_field:32-\>mpls_label,set_field:1-\>mpls_tc,output:s3-eth2
ovs-ofctl -O OpenFlow13 add-flow s3 in_port=s3-eth2,dl_type=0x8847,mpls_tc=0,mpls_label=23,actions=pop_mpls:0x0806,output:s3-eth1
ovs-ofctl -O OpenFlow13 add-flow s3 in_port=s3-eth2,dl_type=0x8847,mpls_tc=1,mpls_label=23,actions=pop_mpls:0x0800,output:s3-eth1

