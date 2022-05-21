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
    h1 = net.addHost(name='h1', ip="10.0.0.1", mac="00:00:00:00:00:01")
    h2 = net.addHost(name='h2', ip="10.0.0.2", mac="00:00:00:00:00:02")
    h3 = net.addHost(name='h3', ip="10.0.0.3", mac="00:00:00:00:00:03")
    h4 = net.addHost(name='h4', ip="10.0.0.4", mac="00:00:00:00:00:04")
    h5 = net.addHost(name='h5', ip="10.0.0.5", mac="00:00:00:00:00:05")
    h6 = net.addHost(name='h6', ip="10.0.0.6", mac="00:00:00:00:00:06")
    h7 = net.addHost(name='h7', ip="10.0.0.7", mac="00:00:00:00:00:07")
    h8 = net.addHost(name='h8', ip="10.0.0.8", mac="00:00:00:00:00:08")

    s1 = net.addSwitch('s1', protocols="OpenFlow13")
    s2 = net.addSwitch('s2', protocols="OpenFlow13")
    s3 = net.addSwitch('s3', protocols="OpenFlow13")
    s4 = net.addSwitch('s4', protocols="OpenFlow13")
    s5 = net.addSwitch('s5', protocols="OpenFlow13")
    s6 = net.addSwitch('s6', protocols="OpenFlow13")
    s7 = net.addSwitch('s7', protocols="OpenFlow13")
    # Add links
    net.addLink(s1,s2)
    net.addLink(s1,s3)
    net.addLink(s2,s4)
    net.addLink(s2,s5)
    net.addLink(s3,s6)
    net.addLink(s3,s7)
    net.addLink(s4,h1)
    net.addLink(s4,h2)
    net.addLink(s5,h3)
    net.addLink(s5,h4)
    net.addLink(s6,h5)
    net.addLink(s6,h6)
    net.addLink(s7,h7)
    net.addLink(s7,h8)

    # Add Controller
    c1 = net.addController(name='c1', ip='127.0.0.1', port=6633)

    s1.start([c1])
    s2.start([c1])
    s3.start([c1])
    s4.start([c1])
    s5.start([c1])
    s6.start([c1])
    s7.start([c1])

    net.build()
    net.start()
    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()

