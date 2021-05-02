def test_encrypt():
    from quarkz.rsa import encrypt

    data = encrypt(33)
    assert(type(data) == dict)
    assert(len(data.keys()) == 7) #make sure all data is there 
    assert(None not in data.values()) #ensure all values are populated 

def test_encrypt_decrypt():
    from quarkz.rsa import encrypt, decrypt

    message = 33 
    data = encrypt(33) 
    message_decrypted = int(decrypt(**data))
    assert(message == message_decrypted)
    
