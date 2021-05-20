#Part1
import ncclient
import xml.dom.minidom

from ncclient import manager

m = manager.connect(
        host = "192.168.56.103",
        port = 830,
        username = "cisco",
        password = "cisco123!",
        hostkey_verify=False,
        )

#Step3
netconf_reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


#Step4
netconf_filter = """
    <filter>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
    </filter>
    """

netconf_reply = m.get_config(source="running", filter = netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

#Part2
#Step2 & 3

netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>NEWHOSTNAME1</hostname>
        <interface>
            <Loopback>
                <name>100</name>
                <description>TEST1</description>
                <ip>
                    <address>
                        <primary>
                            <address>100.100.100.100</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
""" 

netconf_reply = m.edit_config(target="running", config = netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

#Step4
netconf_data = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>NEWHOSTNAME1</hostname>
        <interface>
            <Loopback>
                <name>111</name>
                <description>TEST1</description>
                <ip>
                    <address>
                        <primary>
                            <address>100.100.100.100</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
"""

netconf_reply = m.edit_config(target="running", config = netconf_data)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
