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

netconf_filter = """
<filter>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name/>
            <phys-address/>
            <statistics>
                <in-octets/>
                <out-octets/>
            </statistics>
        </interface>
    </interfaces-state>
</filter>
"""  

netconf_reply = m.get(filter = netconf_filter)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


#Convert XML to Python Dictionary
import xmltodict 
netconf_reply_dict = xmltodict.parse(netconf_reply.xml) 
for interface in netconf_reply_dict["rpc-reply"]["data"]["interfaces-state"]["interface"]: 
    print("Name: {} MAC: {} Input: {} Output {}".format( 
                interface["name"], 
                interface["phys-address"], 
                interface["statistics"]["in-octets"], 
                interface["statistics"]["out-octets"] 
               )
        )
