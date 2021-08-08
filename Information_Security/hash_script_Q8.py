import os
import sys
import hashlib

salt = os.urandom(32)

dk = hashlib.sha512(sys.argv[1].encode('utf-8') + salt).hexdigest()
print(dk)
