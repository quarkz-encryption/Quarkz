from quarkz.rsa import createKey, encrypt, decrypt

key = createKey(1024)

def test_encrypt():
    ciphertext = encrypt(797, key["publicKey"])

def test_encrypt_decrypt():
    message = 98

    ciphertext = encrypt(message, key["publicKey"])

    plaintext = decrypt(ciphertext, key["privateKey"])

    assert(message == plaintext)