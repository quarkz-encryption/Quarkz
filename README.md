# Quarkz

[![Unit Tests](https://github.com/quarkz-encryption/Quarkz/actions/workflows/test.yml/badge.svg)](https://github.com/quarkz-encryption/Quarkz/actions/workflows/test.yml)

[![Upload Release](https://github.com/quarkz-encryption/Quarkz/actions/workflows/python-publish.yml/badge.svg)](https://github.com/quarkz-encryption/Quarkz/actions/workflows/python-publish.yml)

## Documentation

Check out our Documentation that explains how the algorithm works in depth while making references to the code: [Documentation](https://docs.google.com/document/d/1lkPAdd-AOcos1G1m9SIPzCQeUe4DH5eviVi7iuLOt2s/edit?usp=sharing 'Documentation')

## Example

Install the dependencies, then:

```
$ pip3 install -r requirements.txt
$ python3 example.py
```

## How to Install

```
$ pip3 install quarkz
```

## How to Use

First, create a key pair:

```python
from quarkz.utils import createKey

key_pair = createKey(keysize=256) #256 is the recommended keysize
print(key_pair) # --> <quarkz.dtypes.KeyPair object at 0x7f430c33b1c0>
```

Then, encrypt some data. Note you'll need your public key:

```python
from quarkz.quarkz import encrypt

pub_key = key_pair.get_public_key()

some_data = "some string"
encrypted_data = encrypt(some_data, pub_key)

print(encrypted_data) # --> <quarkz.dtypes.Encrypted object at 0x7f430c33b1c0>
```

To decrypt you simply need your keypair created earlier:

```python
from quarkz.quarkz import decrypt

decrypted_data = decrypt(encrypted_data, key_pair)
print(decrypted_data) # --> "some string"

```

## Development Install

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

## How to run pre-built test

First, you will need to set up the environment as shown above.

_Note: Make sure you are in your python3 virtual environment._

Once that is done simply run `string_test.py` in the top directory:

```bash
$ python string_test.py
```
