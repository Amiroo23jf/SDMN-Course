from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def topology():
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
    s1 = net.addSwitch('s1', protocols="OpenFlow13")
    s2 = net.addSwitch('s2', protocols="OpenFlow13")
    s3 = net.addSwitch('s3', protocols="OpenFlow13") # this switch is our router

    # Add links
    net.addLink(h1,s1)
    net.addLink(h2,s2)
    net.addLink(s1,s3)
    net.addLink(s3,s2)

    # Add Controller
    c1 = net.addController(name='c1', ip='127.0.0.1', port=6633)
    s1.start([c1])
    s2.start([c1])
    s3.start([c1])

    net.build()
    net.start()

    # setting default gateway for h1 and h2 (In here we set the hosts as their own gateways)
    h1.cmd("route add default gw 10.0.1.1")
    h2.cmd("route add default gw 10.0.2.1")

    # removing switch flows just to be sure
    s1.cmd("ovs-ofctl -O OpenFlow13 del-flows s1")
    s2.cmd("ovs-ofctl -O OpenFlow13 del-flows s2")
    s3.cmd("ovs-ofctl -O OpenFlow13 del-flows s3")
    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()

