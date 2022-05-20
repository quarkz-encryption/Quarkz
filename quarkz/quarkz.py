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

decimal.getcontext().prec=100000


def encrypt(message: str, publicKey: dict) -> quarkz.dtypes.Encrypted: 

    assert(type(message) == str)

    # 1.3.2   Introducing the Message to be Encrypted
    message = utils.convert_to_int(message)
    
    print ("m: ", message)

    m = Decimal(message)

    # This is really slow find ways to speed up...
    # s = m**publicKey["e"]
    
    #print ("s: ", sys.getsizeof(s)*8)


    # Calculating the count is really slow
    # We want to implement some sort of 
    # modular exponentiation trick to speed this up.

    # 1.3.3   Finding the count: how many times o goes into m**e
    # count = Decimal(int(s) // int(publicKey["o"]))
    # count = Decimal(s)

    # print ("count: ", count)

    # 1.3.4   Generating offset from count and ratio
    # offset = Decimal(count) % Decimal(publicKey["ratio"])

    # print ("ratio: ", publicKey["ratio"])


    offset = Decimal(pow(m, publicKey["e"], publicKey["ratio"]))

    print ("offset: ", offset)
    # 1.3.5   Generating the Ciphertext Using m and e
    # ciphertext = Decimal(pow(m, publicKey["e"], publicKey["o"]))

    ciphertext = 0

    # print ("ciphertext: ", ciphertext)

    # print ("size: ", sys.getsizeof(count//publicKey["ratio"]))

    # 1.3.6   Completed Ciphertext to be Sent To Private Key Holder
    data = {"ciphertext": ciphertext, "offset": offset}

    #print ("ciphertext: ", sys.getsizeof(data["ciphertext"]) + sys.getsizeof(data["offsetCount"]))
    #print ("ciphertext: ", ciphertext)

    return Encrypted(**data)


def decrypt(encrypted: quarkz.dtypes.Encrypted, keypair: quarkz.dtypes.KeyPair) -> int:
    encrypted = vars(encrypted)

    privateKey = keypair.get_private_key()
    # 1.4.1   Finding the complete offset from offset in encryption phase
    offset = round(((encrypted["offset"]) * privateKey["diff"])) % privateKey["n"]

    # 1.4.2   Modifying the ciphertext using the new offset
    ciphertext = int(encrypted["ciphertext"] - offset)

    # 1.4.3   Using Normal RSA Decryption
    plaintext = pow(ciphertext, int(privateKey["d"]), int(privateKey["n"]))

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
