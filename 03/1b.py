from Crypto.Hash import HMAC
import os

print("write password: ")
password = input()
password = password.encode('ascii')

h= HMAC.new(password)

with open('1.txt', 'rb') as infile:
    chunk = infile.read(os.path.getsize('1.txt'))

h.update(chunk)
mac = h.digest()
print(mac)
size = os.path.getsize('1.txt')

f= open ('H.txt', 'rb')
output = f.read(os.path.getsize('H.txt'))

mac2 = output[size:]
print(mac2)
if mac == mac2:
	print('ok')
else:
	print('nok')

