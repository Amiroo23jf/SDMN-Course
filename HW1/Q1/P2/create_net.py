from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
    net = Mininet(
        controller=None,
        switch=OVSKernelSwitch,
        link=TCLink
    )

    # Add hosts and switches
    h1 = net.addHost(name='h1', ip="10.0.1.1/24",
    mac="00:00:00:00:00:01")
    h2 = net.addHost(name='h2', ip="10.0.2.1/24",
    mac="00:00:00:00:00:02")
    r1 = net.addSwitch('r1')
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')
    

    # Add links
    net.addLink(h1,s1)
    net.addLink(h2,s2)
    net.addLink(s1,r1)
    net.addLink(r1,s2)

    net.build()
    net.start()
    
    # setting default gateway for h1 and h2 (In here we set the hosts as their own gateways)
    h1.cmd("route add default gw 10.0.1.1")
    h2.cmd("route add default gw 10.0.2.1")

    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()

