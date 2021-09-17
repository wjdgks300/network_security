from Crypto.Hash import HMAC
import os

print("write password: ")
password = input()
password = password.encode('ascii')

h= HMAC.new(password)

with open('1.txt', 'rb+') as infile:
    chunk = infile.read(os.path.getsize('1.txt'))

h.update(chunk)
mac = h.digest()
print(mac)

chunk += mac

f= open ('H.txt', 'wb')
f.write(chunk) 
f.close()


