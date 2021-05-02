from quarkz.rsa import createKey, encrypt, decrypt

key = createKey(1024)

ciphertext = encrypt(797, key["publicKey"])

plaintext = decrypt(ciphertext, key["privateKey"])

print (plaintext)
