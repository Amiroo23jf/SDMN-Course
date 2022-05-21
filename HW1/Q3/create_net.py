from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.link import TCLink
import numpy as np
import json

def topology(A):
    net = Mininet(
        controller=RemoteController,
        switch=OVSKernelSwitch,
        link=TCLink
    )

    # Add hosts and switches
    h1 = net.addHost(name='h1', ip="10.0.1.1/24",
    mac="00:00:00:00:00:01")
    h2 = net.addHost(name='h2', ip="10.0.2.1/24",
    mac="00:00:00:00:00:02")
    s = []
    n = A.shape[0]
    for i in range(1,n+1):
        s.append(net.addSwitch('s'+str(i), protocols="OpenFlow13"))

    # Add links
    link_list = [] # contains the list of the links that are already created
    port_list = [1] * n
    intf_port_dict = {}
    net.addLink(h1, s[0], intfName1="h1-eth1", intfName2="s1-eth1")
    net.addLink(h2, s[n-1], intfName1="h2-eth1", intfName2="s"+str(n)+"-eth"+str(n))
    intf_port_dict['s1-eth1'] = port_list[0]
    intf_port_dict['s'+str(n)+'-eth'+str(n)] = port_list[n-1]
    port_list[0]+=1
    port_list[n-1]+=1

    for i in range(n):
        for j in range(n):
            link_set = {i,j}
            if A[i,j] != 0:
                if (link_set in link_list) == False :
                    intfName1 = 's'+str(i+1)+'-eth'+str(j+1)
                    intfName2 = 's'+str(j+1)+'-eth'+str(i+1)
                    net.addLink(s[i], s[j], intfName1=intfName1, intfName2=intfName2)
                    
                    # saving the port in the intf to port dict
                    intf_port_dict[intfName1] = port_list[i]
                    intf_port_dict[intfName2] = port_list[j]
                    port_list[i]+=1
                    port_list[j]+=1
                    link_list.append(link_set)
    
    # Saving port-interface dictionary to be used in the future (in create_flows.py)
    with open("data/port_intf_dict.json", "w") as f:
        json.dump(intf_port_dict, f)
    # Add Controller
    c1 = net.addController(name='c1', ip='127.0.0.1', port=6633)
    for i in range(n):
        s[i].start([c1])

    net.build()
    net.start()

    # setting default gateway for h1 and h2 (In here we set the hosts as their own gateways)
    h1.cmd("route add default gw 10.0.1.1")
    h2.cmd("route add default gw 10.0.2.1")

    # removing switch flows just to be sure
    CLI(net)
    net.stop()


