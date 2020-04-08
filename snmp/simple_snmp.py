from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen1 = cmdgen.CommandGenerator()

errorIndication, errorStatus, errorIndex, varBinds = cmdGen1.getCmd(
          cmdgen.CommunityData('public'),
          cmdgen.UdpTransportTarget( ('192.168.1.11', 161)  ),
          cmdgen.MibVariable('SNMPv2-MIB', 'sysDescr'),
          lookupNames=True, lookupValues=True
)



if errorIndication:
    print errorIndication
else:
    for name, val in varBinds:
        print('%s = %s' % (name.prettyPrint(), val.prettyPrint()  ) )

