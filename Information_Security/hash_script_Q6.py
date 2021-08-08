import sys
import hashlib

salt = "Km5d5ivMy8iexuHcZrsD"

dk = hashlib.pbkdf2_hmac('sha512', sys.argv[1].encode('utf-8'), salt.encode('utf-8'), 200000)
print(dk.hex())

