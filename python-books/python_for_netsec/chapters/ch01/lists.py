protocolList = []
protocolList.append("FTP")
protocolList.append("SSH")
protocolList.append("SMTP")
protocolList.append("HTTP")
protocolList.sort()

position = protocolList.index('SSH')
# print("SSH Position "+str(position))

count = len(protocolList)
# print("Protocol elements "+ str(count))

for protocol in protocolList:
    print(protocol)

responses = [200, 400, 403, 500]
responses.append(503)
print(responses)
responses.extend([504,505])
print(responses)
responses.insert(6, 300)
print(responses)

print(protocolList)
protocolList[::-1]
print(protocolList)

