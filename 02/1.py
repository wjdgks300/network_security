
# AES pycrypto package
from Crypto.Cipher import AES

def encryt(message):
	IV = b'IV-0123456789ABC'
	encrypt_AES = AES.new(b'secret-key-01234', AES.MODE_CFB, IV )
	print ("message length: ", len(message))
	ciphertext = encrypt_AES.encrypt(message)
	print("Cipher text: " , ciphertext)
	return ciphertext
	
def decrypted(ciphertext):
	IV = b'IV-0123456789ABC'
	decrypt_AES = AES.new(b'secret-key-01234', AES.MODE_CFB,IV)
	message_decrypted =  decrypt_AES.decrypt(ciphertext)
	print("Decrypted text: ",  message_decrypted.strip())

while True:
	print("input message : ", end= ' ')
	message = input()
	if hasattr(message, 'bitearray'): message.encode('ascii')
	text = encryt(message)
	decrypted(text)




