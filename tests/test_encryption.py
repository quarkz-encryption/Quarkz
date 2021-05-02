def test_encrypt():
    from quarkz.rsa import encrypt
    import quarkz

    data = encrypt(33)

def test_encrypt_decrypt():
    from quarkz.rsa import encrypt, decrypt

    message = 33 
    data = encrypt(33) 
    message_decrypted = int(decrypt(data))
    assert(message == message_decrypted)
    
