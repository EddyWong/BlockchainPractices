import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read

# Generate public and private key pair
keyPair = RSA.generate(1024, random_generator)

publicKey = keyPair.publickey()

message = "But I have to leave"

encryptedText = publicKey.encrypt(message, 32)

print ("Encrypted Text : " + str(encryptedText))

decryptedText = keyPair.decrypt(encryptedText)

print ("Decrypted Text : " + decryptedText)
