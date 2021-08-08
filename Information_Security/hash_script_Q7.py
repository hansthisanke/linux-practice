import sys
import os
import hashlib

salt = os.urandom(32)

dk = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode('utf-8'), salt, 200000)
print(dk.hex())
