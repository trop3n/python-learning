services = {"FTP":21, "SSH":22, "SMTP":25, "HTTP":80}
services2 = {"FTP":21, "SSH":22, "SMTP":25, "LDAP":389}

print(services)
services.update(services2)
print(services)
