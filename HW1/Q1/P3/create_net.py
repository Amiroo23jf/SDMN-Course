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
    h1 = net.addHost(name='h1', ip="10.0.0.1/24", mac="00:00:00:00:00:01")
    h2 = net.addHost(name='h2', ip="10.0.0.2/24", mac="00:00:00:00:00:02")
    h3 = net.addHost(name='h3', ip="10.0.0.3/24", mac="00:00:00:00:00:03")

    s1 = net.addSwitch('s1', protocols="OpenFlow13")
    s2 = net.addSwitch('s2', protocols="OpenFlow13")
    s3 = net.addSwitch('s3', protocols="OpenFlow13")
    # Add links
    net.addLink(h1,s1,intfName1="h1-eth0",intfName2="s1-eth1")
    net.addLink(h2,s2,intfName1="h2-eth0",intfName2="s2-eth1")
    net.addLink(h3,s3,intfName1="h3-eth0",intfName2="s3-eth1")
    net.addLink(s1,s2,intfName1="s1-eth2",intfName2="s2-eth2")
    net.addLink(s2,s3,intfName1="s2-eth3",intfName2="s3-eth2")

    net.build()
    net.start()
    CLI(net)
    net.stop()

if __name__=='__main__':
    topology()

