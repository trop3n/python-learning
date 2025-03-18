protocolList = []
protocolList.append("FTP")
protocolList.append("SSH")
protocolList.append("SMTP")
protocolList.append("HTTP")
# print(protocolList)

protocolList.sort()
# print(protocolList)

# print(type(protocolList))
# print(len(protocolList))

position = protocolList.index('SSH')
# print("SSH Position "+str(position))

protocolList.remove("SSH")
# print(protocolList)

count = len(protocolList)
# print("Protocol elements "+ str(count))

for protocol in protocolList:
    print(protocol)