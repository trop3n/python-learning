services = {"FTP":21, "SSH":22, "SMTP":25, "HTTP":80}
print(services.items())
print(services.keys())
print(services.values())

for key,value in services.items():
    print(key,value)

services['HTTPS'] = 443
print(services)