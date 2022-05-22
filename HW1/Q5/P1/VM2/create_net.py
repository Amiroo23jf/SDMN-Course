from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
import os
def topology():
    net = Mininet(
        controller=None,
        switch=OVSKernelSwitch,
        link=TCLink
    )

    # Add hosts and switches
    h1 = net.addHost(name='h1', ip="10.0.0.2/24")
    h2 = net.addHost(name='h2', ip="10.0.0.2/24")
    s2 = net.addSwitch('s2')

    # Add links
    net.addLink(h1,s2)
    net.addLink(h2,s2)

    net.build()
    net.start()


    os.system('ovs-vsctl --may-exist add-port s2 vxlan2 -- set interface vxlan2 type=vxlan option:key=flow ofport_request=3 option:remote_ip=172.16.178.128')

    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()
