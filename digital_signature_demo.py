from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

random_generator = Random.new().read

# Generate public and private key pair
keyPair = RSA.generate(1024, random_generator)
pubKey = keyPair.publickey()

# The real message we want to send
message = "You know I am missing you."
# Use SHA-256 to hash our message
# https://en.wikipedia.org/wiki/SHA-2
hashA = SHA256.new(message).digest()
# Use generated private key to encrpt the hash of our message
digitalSignature = keyPair.sign(hashA, "")

print ("Hash A: " + repr(hashA) + "\n")
print ("Digital Signature: " + repr(digitalSignature) + "\n")

# Use the same hash algorithm to hash received message
hashB = SHA256.new(message).digest()

print ("Hash B: " + repr(hashB) + "\n")

# Use shared public key to decrypt signature to get
# hash value of orignial message, then compare hash value of
# orignial message with hash value of received one
if (pubKey.verify(hashB, digitalSignature)):
    print "Message hash matched!"
else:
    print "Message hash didn't match!"
