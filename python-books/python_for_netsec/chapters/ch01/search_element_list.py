protocolList = ["FTP", "HTTP", "SNMP", "SSH"]
element_to_find = "SSH"
for x in range(len(protocolList)):
    if element_to_find in protocolList[x]:
        print("Element found at index", x)
        break