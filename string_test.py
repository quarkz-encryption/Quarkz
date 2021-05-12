from quarkz.utils import createKey 
from quarkz.rsa import encrypt, decrypt

if __name__ == "__main__":
    message = input('enter text: ')
    key = createKey(keysize=1024) 
    pub = key.get_public_key() 
    print(f'message: {message}')
    encrypted_data = encrypt(message, pub) 

    decrypted_data = decrypt(encrypted_data, key) 
    print(f'end message: {decrypted_data}!')
