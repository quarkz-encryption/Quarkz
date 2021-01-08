#!/usr/bin/env python3
import random
from Crypto.Util import number
from Crypto.PublicKey import RSA

class KeyGenerator():
    def __init__(self):
        self.name = 'tavian'

    def pri(self):
        print (self.name)