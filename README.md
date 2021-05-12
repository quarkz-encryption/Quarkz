# Quarkz
[![Unit Tests](https://github.com/quarkz-encryption/Quarkz/actions/workflows/test.yml/badge.svg)](https://github.com/quarkz-encryption/Quarkz/actions/workflows/test.yml)

A mathematically beautiful encryption library
## Example 
Install the dependencies, then: 
```
$ python3 example.py 
```

## How to Use
First, create a key pair:
```python 
from quarkz.utils import createKey

key_pair = createKey(keysize=2048)
print(key_pair) # --> <quarkz.dtypes.KeyPair object at 0x7f430c33b1c0>
```

Then, encrypt some data. Note you'll need your public key:
```python
from quarkz.rsa import encrypt

pub_key = key_pair.get_public_key()

some_data = 41
encrypted_data = encrypt(some_data, pub_key)

print(encrypted_data) # --> <quarkz.dtypes.Encrypted object at 0x7f430c33b1c0>
```

To decrypt you simply need your keypair created earlier: 
```python
from quarkz.rsa import decrypt

decrypted_data = decrypt(encrypted_data, key_pair)
print(decrypted_data) # --> 41

```



## How to Install 

For development, it is recommended to use a virtual env: 
```
$ python3 -m venv env
```
To activate it: 
```
$ source env/bin/activate
```
or when using the fish shell:
```
$ source env/bin/activate.fish
```

To install:
```
$ pip3 -r requirements.txt
```
