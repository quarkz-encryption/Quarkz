import random
import sys
import json
import decimal

from base64 import b64encode, b64decode
from decimal import Decimal

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import number
from Crypto.PublicKey import RSA 

from quarkz import utils 
from quarkz.dtypes import Encrypted 
import quarkz

decimal.getcontext().prec=5000


def encrypt(message: str, publicKey: dict) -> quarkz.dtypes.Encrypted: 

    assert(type(message) == str)

    message = utils.convert_to_int(message)

    m = Decimal(message)

    # This is really slow find ways to speed up...
    s = m**publicKey["e"]
    
    #print ("s: ", sys.getsizeof(s)*8)


    # Calculating the count is really slow
    # We want to implement some sort of 
    # modular exponentiation trick to speed this up.
    count = Decimal(int(s) // int(publicKey["o"]))

    #print (count)

    #print(sys.getsizeof(count))

    offsetCount = Decimal(count) % Decimal(publicKey["ratio"])

    ciphertext = Decimal(pow(m, publicKey["e"], publicKey["o"]))

    data = {"ciphertext": ciphertext, "offsetCount": offsetCount}

    #print ("ciphertext: ", sys.getsizeof(data["ciphertext"]) + sys.getsizeof(data["offsetCount"]))
    #print ("ciphertext: ", ciphertext)

    return Encrypted(**data)


def decrypt(encrypted: quarkz.dtypes.Encrypted, keypair: quarkz.dtypes.KeyPair) -> int:
    encrypted = vars(encrypted)

    privateKey = keypair.get_private_key()

    offset = round(((encrypted["offset"]) * privateKey["diff"])) % privateKey["n"]

    ciphertext = int(encrypted["ciphertext"] - offset)

    plaintext = pow(ciphertext, int(privateKey["d"]), int(privateKey["n"]))

    #print (plaintext)
    
    if plaintext:
        return utils.convert_to_str(plaintext)
    else: 
        ciphertext = int(encrypted["ciphertext"] + offset)
        return pow(ciphertext, int(privateKey["d"]), int(privateKey["n"]))



if __name__ == "__main__":
    #first, create a new key pair 
    pair = utils.createKey(1024)

    #encrypt some data
    message = 69
    public_key = pair.get_public_key()
    encrypted_data = encrypt(message, public_key)

    #decrypt the data again
    decrypted_data = decrypt(encrypted_data, pair)
    print(decrypted_data)
