from quarkz.quarkz import encrypt, decrypt
from quarkz.utils import createKey

def test_create_key():
    key_pair = createKey()

key_pair = createKey(keysize=1024)

def test_encrypt():
    public_key = key_pair.get_public_key()
    encrypted_data = encrypt("this is a test", public_key)


def test_encrypt_decrypt():
    m = "this is a test"
    public_key = key_pair.get_public_key()
    encrypted_data = encrypt(m, public_key)

    decrypted_data = decrypt(encrypted_data, key_pair)
    assert(m == decrypted_data)
